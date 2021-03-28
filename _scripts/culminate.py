#!/usr/bin/env python3

from json import dumps
from os import environ
from urllib.request import Request, urlopen

# parameters
origin = 'https://www.ashenm.ml'
hrefs = [ origin ]

# construct file hrefs
with open('artifacts.txt') as artifacts:
  hrefs.extend([ '{}{}'.format(origin, artifact.strip()) for artifact in artifacts ])

# verbose parameters on CI
if environ.get('CI'):
  print(dumps(hrefs, indent=2))

# purge CloudFlare cache
# https://api.cloudflare.com/#zone-purge-files-by-url
urlopen(Request(
  method='POST',
  data=dumps({ 'files': hrefs }).encode('utf-8'),
  headers={
    'Authorization': 'Bearer {}'.format(environ['CLOUDFLARE_TOKEN']),
    'Content-Type': 'application/json'
  },
  url='https://api.cloudflare.com/client/v4/zones/{}/purge_cache'.format(environ['CLOUDFLARE_ZONE_ID'])
))
