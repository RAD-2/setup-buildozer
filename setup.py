#! /usr/bin/python3
import os
from N4Tools import System,Design

commands = [
    'sudo apt-get install python3-setuptools',
    'sudo apt install git',o
    'git clone https://github.com/kivy/buildozer.git',
    'cd buildozer',
    'sudo python3 setup.py install',
    'sudo apt update',
    'sudo apt install -y git zip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5ade cython virtualenv',
    'sudo apt-get install cython',
    'python3 -m pip install cython',
]

os.chdir(os.environ['HOME'])
for i in commands:
    os.system(i)

try:
    Error = False
    if all([
            System.is_in_home('buildozer'),
            System.is_in_home('.buildozer'),
            System.is_in_bin('buildozer'),
            ]):
        try:
            import Cython
        except:
            Error = True
    else:
        Error = True

finally:
    msg = 'GL## Done...'
    if Error:msg = 'RL## Error...'
    print(Design.Color.reader(msg))
