#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    line_param = int(sys.argv[1])
except IndexError as e:
    print("Usage: 13.py num")
    sys.exit(1)

with open("hightemp.txt", "r") as fp:
    texts = []
    for (i, line) in enumerate(fp):
        texts.append(line)

    print("".join(texts[i - line_param + 1:i - line_param + line_param + 1]).rstrip("\r\n"))



