#!/usr/bin/env python3

from os import P_WAIT, remove, spawnlp

spawnlp(P_WAIT, 'bundle', 'bundle', 'install')
spawnlp(P_WAIT, 'pip3', 'pip3', 'install', '--requirement', 'requirements.txt')
