#!/usr/bin/env python3

import os

# build custom routes
os.spawnlp(os.P_WAIT, 'python3', 'python', '.travis/routes.py')

# build site
os.spawnlp(os.P_WAIT, 'jekyll', 'jekyll', 'build')
