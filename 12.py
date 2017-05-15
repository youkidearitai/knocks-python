#!/usr/bin/env python
# -*- coding: utf-8 -*-

col1 = []
col2 = []

with open("Hightemp.txt", "r") as fp:
    for line in fp:
        cols = line.split("\t")
        col1.append(cols[0])
        col2.append(cols[1])

with open("col1.txt", "w") as fp:
    for col in col1:
        fp.write(col)
        fp.write("\n")

with open("col2.txt", "w") as fp:
    for col in col2:
        fp.write(col)
        fp.write("\n")

