#!/usr/bin/env python3

from yaml import load

with open('_data/routes.yml', 'r') as file:
  for route in load(file):
    with open('{}.html'.format(route['path']), 'w') as file:
      file.write(
        '---\n'
        'title: {}\n'
        'permalink: /{}\n'
        'redirect_to:\n'
        '  - {}\n'
        '---\n'
      .format(route['path'].capitalize(), route['path'], route['url']))
