#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    line_param = int(sys.argv[1])
except IndexError as e:
    print("Usage: 14.py num")
    sys.exit(1)

with open("hightemp.txt", "r") as fp:
    texts = []
    for (i, line) in enumerate(fp):
        if i < line_param:
            print(line.rstrip("\r\n"))
        else:
            break
