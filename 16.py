#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    line_param = int(sys.argv[1])
except IndexError as e:
    print("Usage: 15.py num")
    sys.exit(1)

with open("hightemp.txt", "r") as fp:
    lines = []
    files = []
    for (i, line) in enumerate(fp):
        if i % line_param == line_param - 1:
            files.append(lines)
            lines = []
        lines.append(line)

for (i, f) in enumerate(files):
    with open("hightemp{0}.txt".format(chr(ord('a') + i)), "w") as fp:
        for line in f:
            fp.write(line)


