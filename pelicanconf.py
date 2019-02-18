#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'

THEME = 'FlexTheme'

AUTHOR = 'Anders Rye Jacobsen'
SITETITLE = AUTHOR
SITENAME = 'Anders\' Blog'
SITESUBTITLE = '<br>Economics student who loves everything<br> technology, coding and data-science'
SITEDESCRIPTION = 'My thoughts and writings about technology, data-science, life and everything in between'

FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'default'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

COPYRIGHT_YEAR = f'{AUTHOR} 2019'

DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
MENUITEMS = (('Archive', '/archives'), ('Categories', '/categories'),)

# Social widget
SOCIAL = (('linkedin', 'https://linkedin.com/in/anders-rye-jacobsen'),
          ('github', 'https://github.com/ismand95'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
