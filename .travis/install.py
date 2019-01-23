#!/usr/bin/env python3

import os

os.spawnlp(os.P_WAIT, 'bundle', 'bundle', 'install')
os.spawnlp(os.P_WAIT, 'pip', 'pip', 'install', '--user', 'pyyaml')
