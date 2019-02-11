#!/usr/bin/env python3

import os
from urllib.request import urlopen

# build custom routes
os.spawnlp(os.P_WAIT, 'python3', 'python', '.travis/routes.py')

# build site
os.spawnlp(os.P_WAIT, 'jekyll', 'jekyll', 'build')

# fetch resume.html
with open(file='resume.html', mode='wb') as file:
  file.write(urlopen('https://raw.githubusercontent.com/ashenm/xmlresume/gh-pages/resume.html').read())

# fetch resume.pdf
with open(file='resume.pdf', mode='wb') as file:
  file.write(urlopen('https://raw.githubusercontent.com/ashenm/xmlresume/gh-pages/resume.pdf').read())
