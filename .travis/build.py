#!/usr/bin/env python3

import os

# build custom routes
print('travis_fold:start:build_routes\033[33;1mbuild routes\033[0m')
os.spawnlp(os.P_WAIT, 'python3', 'python', '.build/routes.py')
print('\ntravis_fold:end:build_routes\r')

# build site
print('travis_fold:start:build_site\033[33;1mbuild site\033[0m')
os.spawnlp(os.P_WAIT, 'jekyll', 'jekyll', 'build')
print('\ntravis_fold:end:build_site\r')
