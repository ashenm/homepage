#!/usr/bin/env python3
# Prepare CI Environment

from os import P_WAIT, spawnlp

# update package lists
spawnlp(P_WAIT, 'sudo', 'sudo', 'apt-get', 'update')

# install ruby header file
spawnlp(P_WAIT, 'sudo', 'sudo', 'apt-get', 'install', '--yes', 'ruby-dev')

# install python dependencies
spawnlp(P_WAIT, 'sudo', 'sudo', 'apt-get', 'install', '--yes', 'python3-pip', 'python3-setuptools', 'python3-wheel')
