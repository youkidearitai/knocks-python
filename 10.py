#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 0
with open("hightemp.txt", "r") as fp:
    for f in fp:
        count += 1

print(count)

# 内包表記とsumをつかったすごい簡素なやつ すごい
with open("hightemp.txt", "r") as fp:
    count = sum(1 for line in fp)

print(count)
