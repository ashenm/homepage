#!/usr/bin/env python3

import os
from yaml import load

# clean generated routes
with open('_data/routes.yml') as file:
  for route in load(file):
    try:
      os.remove('{}.html'.format(route['path']))
    except:
      pass

# clean jekyll build artifacts
os.spawnlp(os.P_WAIT, 'jekyll', 'jekyll', 'clean')
