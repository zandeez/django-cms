.. django cms documentation master file, created by
   sphinx-quickstart on Tue Sep 15 10:47:03 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

######################################
Welcome to django CMS's documentation!
######################################

This document refers to version |release|

*******
Install
*******

.. warning::
    In version 2.4 migrations have been completely rewritten to fix issues
    with newer south releases.
    If upgrading from prior 2.3.2 releases, please refer to
    :ref:`migrations-upgrade`


.. toctree::
    :maxdepth: 1

    getting_started/installation
    upgrade/2.4
    upgrade/2.3.3
    upgrade/2.3.2
    upgrade/2.3
    upgrade/2.2
    upgrade/2.1


***************
Getting Started
***************

.. toctree::
    :maxdepth: 2
    :numbered:

    getting_started/tutorial
    getting_started/using_south
    getting_started/configuration
    getting_started/navigation
    getting_started/plugin_reference
    faq/common_issues
    

********
Advanced
********

.. toctree::
    :maxdepth: 2
    :numbered:
       
    advanced/i18n
    advanced/sitemap
    advanced/templatetags
    advanced/cli
    advanced/permissions_reference


*****************
Extending the CMS
*****************

.. toctree::
    :maxdepth: 2
    :numbered:

    extending_cms/extending_examples
    extending_cms/custom_plugins
    extending_cms/app_integration
    extending_cms/api_references
    extending_cms/placeholders
    extending_cms/searchdocs
    extending_cms/fields


********
Concepts
********

.. toctree::
    :maxdepth: 2
    :numbered:

    concepts/introduction
    concepts/menu_system
    concepts/multiple_languages


**************************
Contributing to django CMS
**************************

.. toctree::
    :maxdepth: 2
    :numbered:

    contribution



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
