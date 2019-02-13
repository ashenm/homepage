#!/usr/bin/env python3

from json import dumps
from os import environ
from urllib.request import Request, urlopen

# parameters
origin = 'https://www.ashenm.ml'
hrefs = [ origin ]

# construct file hrefs
with open('.artifacts') as artifacts:
  hrefs.extend([ '{}{}'.format(origin, artifact.strip()) for artifact in artifacts ])

# purge CloudFlare cache
# https://api.cloudflare.com/#zone-purge-files-by-url
urlopen(Request(
  method='POST',
  url='https://api.cloudflare.com/client/v4/zones/{}/purge_cache'.format(environ['CLOUDFLARE_ZONE_ID']),
  data=dumps({ 'files': hrefs }).encode('utf-8'),
  headers={
    'Content-Type': 'application/json',
    'X-Auth-Email': environ['CLOUDFLARE_USER'],
    'X-Auth-Key': environ['CLOUDFLARE_TOKEN']
  }
))
