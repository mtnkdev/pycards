#!/usr/bin/env python
# -*- mode: python; -*-

import os
from distutils.core import setup

PACKAGE_URL = ""
VERSION = '1.0'

if os.name == 'nt':
    import py2exe

if os.name == 'posix':
    data_dir = 'share/PyCards'
elif os.name == 'nt':
    data_dir = 'data'
else:
    data_dir = 'data'

ddirs = [
    'html',
    'images',
    'tiles',
    'toolbar',
    'themes',
    'tcl',
    ]
##for s in file('MANIFEST.in'):
##    if s.startswith('graft cardsets/cardset-'):
##        ddirs.append(s[11:].strip())

data_files = []

for d in ddirs:
    for root, dirs, files in os.walk(os.path.join('data', d)):
        if root.find('.svn') >= 0:
            continue
        if files:
            #files = map(lambda f: os.path.join(root, f), files)
            files = [os.path.join(root, f) for f in files]
            data_files.append((os.path.join(data_dir, root[5:]), files))

if os.name == 'posix':
    data_files.append(('share/pixmaps', ['data/pysol.xbm', 'data/pysol.xpm']))
    data_files.append(('share/icons',
                       ['data/images/misc/pysol01.png',
                        'data/images/misc/pysol02.png',]))
    for l in ('ru', 'ru_RU'):
        data_files.append(('share/locale/%s/LC_MESSAGES' % l,
                           ['locale/%s/LC_MESSAGES/pysol.mo' % l]))
    data_files.append((data_dir, ['data/pysolfc.glade']))
    data_files.append(('share/applications', ['data/pysol.desktop']))

#from pprint import pprint; pprint(data_files)
#import sys; sys.exit()

long_description = '''\
PyCards is a collection of solitaire card games.
Its features include modern look and feel (uses Tile widget set), multiple
cardsets and tableau backgrounds and lots of documentation.
'''

kw = {
    'name'         : 'PyCards',
    'version'      : VERSION,
    'url'          : PACKAGE_URL,
    'author'       : 'Aravi, Michael, Nikhil',
    'description'  : 'Python solitaire game collection',
    'long_description' : long_description,
    'license'      : 'GPLv3',
    'scripts'      : ['pysol.py'],
    'packages'     : ['source'],
    'data_files'   : data_files,
    }
    
if os.name == 'nt':
    kw['windows'] = [{'script': 'pysol.py',
                      'icon_resources': [(1, 'data/pysol.ico')], }]    

setup(**kw)

setup(windows=['pysol.py'], zipfile=None)
