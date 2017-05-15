#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("Hightemp.txt", "r") as fp:
    for line in fp:
        print(line.replace("\t", " ").rstrip("\r\n"))
