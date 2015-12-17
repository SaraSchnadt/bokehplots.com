#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bokeh contributors'
SITENAME = 'Bokeh'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Nav Links
NAV = (
    ('About', '/pages/about-bokeh.html'),
    ('Gallery', '//bokeh.pydata.org/en/latest/docs/gallery.html'),
    ('Docs', '//bokeh.pydata.org/en/latest/'),
    ('Github', '//github.com/bokeh/bokeh'),
)
# Community Links
COMMUNITY = (
    ('Contribute', '#'),
    ('Join our mailing list', '#')
)
# About Links
ABOUT = (
    ('Team', '#'),
    ('Technical vision', '#'),
    ('Contact', '/pages/contact.html')
)
# Social widget
SOCIAL = (
    ('Github', '#'),
    ('Twitter', '#'),
    ('Youtube', '#')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
