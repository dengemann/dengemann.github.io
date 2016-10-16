#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import bibtexparser

# DATA ########################################################################


def make_nice_author(author, emphasize=('Engemann<sup>&#10033;</sup>, D.', 'Engemann, D.',)):
    split_author = author.split(' and ')
    insert_pos = len(split_author) - 1
    names_split = [au.split(', ') for au in split_author]
    names = ['{}, {}.'.format(n[0], n[1][:1]) for n in names_split]
    author_edit = ', '.join(names[:insert_pos]) + ' and ' + names[insert_pos]
    # print(author_edit)
    if emphasize:
        for emp in emphasize:
            if emp in author_edit:
                # print(emp)
                author_edit = author_edit.replace(
                    emp, '<strong><em>' + emp + '</em></strong>')
    return author_edit

""" XXX
- make sure not to use unicode or LaTeX code
- only full author records, in "surname, name and" format
"""

with open('./data/biblio.bib') as bib:
    bib_str = bib.read()

records = bibtexparser.loads(bib_str)
for item in records.entries:
    item['author'] = make_nice_author(item['author'])

records.entries.sort(key=lambda record: record['year'], reverse=True)

PUBLICATION_LIST = records.entries[:]

COLLABORATORS_LIST = [
    ('Dr. Dr. Danilo Bzdok',
     'Prof. for Social and Affective Neuroscience, RWTH University',
     'Aachen, Germany',
     'https://danilobzdok.de/'),
    ('Laurent Cohen, PhD, MD',
     'Prof. of Neurology, senior scientist at Brain and Spine institute (ICM)',
     'Paris',
     'https://sites.google.com/site/neuropsycho'
     'logyandneuroimaging/laurent-cohen-1'),
    ('Stanislas Dehaene, PhD',
     'Prof. at Collège de France, senior researcher at Neurospin',
     'Paris',
     'https://en.wikipedia.org/wiki/Stanislas_Dehaene'),
    ('Alexandre Gramfort',
     'PhD, Prof. of signal image processing,'
     ' Télécom ParisTech',
     'Paris',
     'http://alexandre.gramfort.net'),
    ('Nathalie George',
     'PhD, senior scientist at ICM',
     'Paris',
     'http://cogimage.dsi.cnrs.fr/perso/ngeorge/ngeorge.htm'),
    ('Matti Hämäläienen',
     'Prof. in Radiology, Harvard Medical School, MEG and EEG expert',
     'Boston, USA',
     'https://www.martinos.org/user/5923'),
    ('Lionel Naccache, PhD, MD',
     'Prof. of Neurology, senior scientist at ICM',
     'Paris',
     'http://icm-institute.org/en/member/?user=988'),
    ('Anders Leverman, PhD',
     'Prof. of climate physics, Potsdamm Institute for climate change research',
     'Potsdamm, Germany',
     'http://www.pik-potsdam.de/~anders/'),
    ('Dr. Manuel Schabus',
     'Prof. of Psychology',
     'Salzburg, Austria',
     'http://www.sleepscience.at/en/team'),
    ('Jacob Sitt, PhD, MD',
     'senior scientist at ICM',
     'Paris',
     None),
    ('Dr. Dr. Kai Vogeley',
     'Prof. of Psychiatry, autism and social cognition expert',
     'Cologne, Germany',
     None),
    ('Gaël Varoquaux, PhD',
     'senior researcher at INRIA and Neurospin, expert for machine learning in brain imaging',
     'Paris',
     'http://gael-varoquaux.info/'),
    ('Virginie van Wassenhove, PhD',
     'senior scientist at Neurospin, expert for oscillatory brain dynamics',
     'Paris',
     'https://sites.google.com/site/virginievanwassenhove/')
]

for test1, test2, test3, test4 in COLLABORATORS_LIST:
    pass  # test data consistency

###############################################################################

AUTHOR = 'Denis A. Engemann'
SITENAME = 'Denis A. Engemann'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
THEME = "themes/pure-single"
# COVER_IMG_URL = 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Cajal_Retina.jpg'
COVER_IMG_URL = './images/cajal.jpg'
PROFILE_IMG_URL = './images/dngman_avatar2.jpg'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = (
    ('github', 'https://github.com/dengemann/'),
    ('twitter-square', 'https://twitter.com/dngman')
    # ('ai-google-scholar-square', 'https://scholar.google.de/citations?user=ombAzhMAAAAJ&hl=en')
)
# for scholar a hack is needed, see base.html

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GOOGLE_ANALYTICS = 'UA-74622344-1'
STATIC_PATHS = ['images', 'pdfs', 'widgets']
PAGE_EXCLUDES = ['widgets', '.ipynb_checkpoints']
ARTICLE_EXCLUDES = ['widgets', '.ipynb_checkpoints']
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DEFAULT_DATE = 'fs'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

# MD_EXTENSIONS = ['codehilite(css_class=highlight,guess_lang=False,linenums=False)',
# 				 'headerid',
#                  'extra']

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATHS = ['../pelican-plugins']

PLUGINS = [
    # 'pelican_plugin-render_math',
	# 'summary',
	# 'neighbors',
    # 'ipynb',
]

DEFAULT_CATEGORY = ''

DIRECT_TEMPLATES = ('index', 'archives')

ARCHIVES_SAVE_AS = 'archives/index.html'

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = ''

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''

DATE_FORMATS = {
    'en': '%Y-%m-%d',
}

# Feed generation is usually not desired when developing
# FEED_ATOM = 'feeds/atom.xml'
# FEED_RSS = 'feeds/rss.xml'
