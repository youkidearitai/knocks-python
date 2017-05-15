#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("hightemp.txt", "r") as fp:
    pref_list = {line.split("\t")[0] for line in fp}

for pref in pref_list:
    print(pref)
