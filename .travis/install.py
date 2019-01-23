#!/usr/bin/env python3

import os

os.spawnlp(os.P_WAIT, 'bundle', 'bundle', 'install')
os.spawnlp(os.P_WAIT, 'pip3', 'pip', 'install', '--user', 'pyyaml')
