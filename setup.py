#! /usr/bin/python3
import os
from N4Tools import System,Design

commands = [
    'sudo apt-get install python3-setuptools',
    'sudo apt install git',
    'git clone https://github.com/kivy/buildozer.git',
    'cd buildozer',
    'sudo python3 setup.py install',
    'sudo apt update',
    'sudo apt install -y git zip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev',
    'pip3 install --user --upgrade cython virtualenv',
    'sudo apt-get install cython',
    'python3 -m pip install cython',
]

os.chdir(os.environ['HOME'])
for i in commands:
    os.system(i)
if all([
        System.is_in_home('buildozer'),
        System.is_in_home('.buildozer'),
        System.is_in_bin('buildozer'),
        ]):
    msg = Design.Color.reader('GL## Done...')
    print(msg)

else:
    msg = Design.Color.reader('RL## Error...')
    print(msg)
