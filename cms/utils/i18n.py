# -*- coding: utf-8 -*-
from contextlib import contextmanager
from cms.exceptions import LanguageError
from django.conf import settings
from django.utils import translation

@contextmanager
def force_language(new_lang):
    old_lang = translation.get_language()
    if old_lang != new_lang:
        translation.activate(new_lang)
    yield
    translation.activate(old_lang)


def get_language_list(site_id=None):
    """
    :return: returns a list of iso2codes for this site
    """
    site_id = get_site(site_id)
    languages = []
    for language in settings.CMS_LANGUAGES[site_id]:
        languages.append(language['code'])
    return languages


def get_language_tuple(site_id=None):
    """
    :return: returns an list of tuples like the old CMS_LANGUAGES or the LANGUAGES for this site
    """
    site_id = get_site(site_id)
    languages = []
    for language in settings.CMS_LANGUAGES[site_id]:
        languages.append((language['code'], language['name']))
    return languages


def get_language_dict(site_id=None):
    """
    :return: returns an dict of cms languages
    """
    site_id = get_site(site_id)
    languages = {}
    for language in settings.CMS_LANGUAGES[site_id]:
        languages[language['code']] = language['name']
    return languages


def get_public_languages(site_id=None):
    """
    :return: list of iso2codes of public languages for this site
    """
    languages = []
    for language in get_language_objects(site_id):
        if language["public"]:
            languages.append(language['code'])
    return languages


def get_language_object(language_code, site_id=None):
    """
    :param language_code: RFC5646 language code
    :return: the language object filled up by defaults
    """
    site_id = get_site(site_id)
    for language in settings.CMS_LANGUAGES[site_id]:
        if language['code'] == language_code:
            return language
    raise LanguageError('Language not found: %s' % language_code)


def get_language_objects(site_id=None):
    """
    returns list of all language objects filled up by default values
    """
    site_id = get_site(site_id)
    languages = []
    for language in settings.CMS_LANGUAGES[site_id]:
        languages.append(get_language_object(language['code'], site_id))
    return languages


def get_default_language(language_code=None):
    """
    Returns default language depending on settings.LANGUAGE_CODE merged with
    best match from settings.CMS_LANGUAGES

    Returns: language_code
    """

    if not language_code:
        language_code = settings.LANGUAGE_CODE

    languages = get_language_list()

    # first try if there is an exact language
    if language_code in languages:
        return language_code

    # otherwise split the language code if possible, so iso3
    language_code = language_code.split("-")[0]

    if not language_code in languages:
        return settings.LANGUAGE_CODE

    return language_code


def get_fallback_languages(language, site_id=None):
    """
    returns a list of fallback languages for the given language
    """
    site_id = get_site(site_id)
    language = get_language_object(language, site_id)
    return language.get('fallbacks', [])

def get_redirect_on_fallback(language, site_id=None):
    """
    returns if you should redirect on language fallback
    :param language:
    :param site_id:
    :return: Boolean
    """
    site_id = get_site(site_id)
    language = get_language_object(language, site_id)
    return language.get('redirect_on_fallback', True)

def hide_untranslated(language, site_id=None):
    """
    Should untranslated pages in this language be hidden?
    :param language:
    :param site_id:
    :return: A Boolean
    """
    site_id = get_site(site_id)
    language = get_language_object(language, site_id)
    return language.get('hide_untranslated', True)

def get_site(site):
    if site is None:
        return settings.SITE_ID
    else:
        try:
            return int(site)
        except TypeError:
            return site.pk
