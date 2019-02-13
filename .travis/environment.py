#!/usr/bin/env python3
# Prepare CI Environment

from os import P_WAIT, spawnlp

# update package lists
spawnlp(P_WAIT, 'sudo', 'sudo', 'apt-get', 'update')

# install pip3
spawnlp(P_WAIT, 'sudo', 'sudo', 'apt-get', 'install', '--yes', 'python3-pip')
