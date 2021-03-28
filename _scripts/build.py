#!/usr/bin/env python3

from bs4 import BeautifulSoup
from datetime import datetime
from glob import iglob
from os import P_WAIT, spawnlp
from re import sub
from shutil import copyfile
from subprocess import DEVNULL, PIPE, run
from urllib.request import urlopen

# build custom routes
spawnlp(P_WAIT, 'python3', 'python', '_scripts/routes.py')

# fetch resume.html
with open(file='resume.html', mode='wb') as file:
  file.write(urlopen('https://raw.githubusercontent.com/ashenm/xmlresume/gh-pages/resume.html').read())

# fetch resume.pdf
with open(file='resume.pdf', mode='wb') as file:
  file.write(urlopen('https://raw.githubusercontent.com/ashenm/xmlresume/gh-pages/resume.pdf').read())

# fetch base template
with open(file='_includes/base.html', mode='rt') as file:
  template = file.read()

# pre-process base template
template = sub(r'<!-- macro:build: build-commit: -->', f'<meta name="build-commit" content="{run([ "git", "rev-parse", "HEAD" ], stdout=PIPE, stderr=DEVNULL).stdout.decode().strip()}" />', template)
template = sub(r'<!-- macro:build: build-timestamp: -->', f'<meta name="build-timestamp" content="{datetime.utcnow().ctime()}" />', template)

# save pre-processed base template
with open(file='_includes/base.html', mode='wt') as file:
  file.write(template)

# build site
spawnlp(P_WAIT, 'bundle', 'bundle', 'exec', 'jekyll', 'build', '--profile')

# sitemap.xml
with open(file='_site/sitemap.xml', mode='r+t') as stream:

  sitemap = BeautifulSoup(stream, 'lxml-xml')

  for loc in sitemap.find_all('loc'):

    if not loc.string.endswith('.html'):
      continue

    loc.string = sub(r'\.html$', '', loc.string)

  stream.seek(0)
  stream.write(str(sitemap))

# list artifacts for cache purging
with open(file='artifacts.txt', mode='wt') as file:
  file.writelines([ '{}\n'.format(path.replace('_site', '')) for path in iglob('_site/**', recursive=True) ])
