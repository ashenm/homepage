#!/usr/bin/env python3

from os import P_WAIT, spawnlp, walk
from urllib.request import urlopen

# build custom routes
spawnlp(P_WAIT, 'python3', 'python', '.travis/routes.py')

# build site
spawnlp(P_WAIT, 'jekyll', 'jekyll', 'build')

# fetch resume.html
with open(file='resume.html', mode='wb') as file:
  file.write(urlopen('https://raw.githubusercontent.com/ashenm/xmlresume/gh-pages/resume.html').read())

# fetch resume.pdf
with open(file='resume.pdf', mode='wb') as file:
  file.write(urlopen('https://raw.githubusercontent.com/ashenm/xmlresume/gh-pages/resume.pdf').read())

# list artifacts for cache purging
with open(file='.artifacts', mode='wt') as file:
  for (folder, folders, artifacts) in walk('_site'):
    file.writelines([ '{}/{}\n'.format(folder.replace('_site', ''), artifact) for artifact in artifacts ])
