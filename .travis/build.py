#!/usr/bin/env python3

from bs4 import BeautifulSoup
from glob import iglob
from os import P_WAIT, spawnlp
from re import sub
from shutil import copyfile
from urllib.request import urlopen

# build custom routes
spawnlp(P_WAIT, 'python3', 'python', '.travis/routes.py')

# fetch resume.html
with open(file='resume.html', mode='wb') as file:
  file.write(urlopen('https://raw.githubusercontent.com/ashenm/xmlresume/gh-pages/resume.html').read())

# fetch resume.pdf
with open(file='resume.pdf', mode='wb') as file:
  file.write(urlopen('https://raw.githubusercontent.com/ashenm/xmlresume/gh-pages/resume.pdf').read())

# list artifacts for cache purging
with open(file='.artifacts', mode='wt') as file:
  file.writelines([ '{}\n'.format(path.replace('_site', '')) for path in iglob('_site/**', recursive=True) ])

# build site
spawnlp(P_WAIT, 'bundle', 'bundle', 'exec', 'jekyll', 'build', '--profile')

# sitemap.xml
with open(file='sitemap.xml', mode='wt') as destination, open(file='_site/sitemap.xml', mode='rb') as source:

  sitemap = BeautifulSoup(source, 'lxml-xml')

  for loc in sitemap.find_all('loc'):

    if not loc.string.endswith('.html'):
      continue

    loc.string = sub(r'\.html$', '', loc.string)

  destination.write(str(sitemap))

# robot.txt
copyfile('_site/robots.txt', 'robots.txt')
