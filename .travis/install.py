#!/usr/bin/env python3

import os

os.spawnlp(os.P_WAIT, 'bundle', 'bundle', 'install')
