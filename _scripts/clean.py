#!/usr/bin/env python3

from os import P_WAIT, remove, spawnlp
from yaml import BaseLoader, load

# build artifacts
excludes = [
  '.artifacts',
  'resume.pdf',
  'resume.html',
  'robots.txt',
  'sitemap.xml'
]

# clean build artifacts
for exclude in excludes:
  try:
    remove(exclude)
  except:
    pass

# clean generated routes
with open('_data/routes.yml') as file:
  for route in load(file, Loader=BaseLoader):
    try:
      remove('{}.html'.format(route['path']))
    except:
      pass

# clean jekyll build artifacts
spawnlp(P_WAIT, 'bundle', 'bundle', 'exec', 'jekyll', 'clean')
