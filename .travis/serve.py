#!/usr/bin/env python3

import os

# serve build locally
os.spawnlp(os.P_WAIT, 'jekyll', 'jekyll', 'serve', '--port', '8080', '--host', '0.0.0.0')
