#!/usr/bin/env python3
import sys
from subprocess import Popen, PIPE, STDOUT, run

try:
    input_stream = sys.stdin.buffer
except AttributeError:
    input_stream = sys.stdin

path = sys.argv[0].rsplit("/", 1)[0]
p = Popen([path + '/on-modify.timewarrior'], stdin=PIPE)
p.communicate('{}\n'.encode() + sys.stdin.readline().encode())
