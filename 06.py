#!/usr/bin/env python
# -*- coding: utf-8 -*-

sourcex = "paraparaparadise"
sourcey = "paragraph"

def bigram(string, n = 2):
    return set(string[s:s+n] for s in range(0, len(string) - n + 1))

x = bigram(sourcex)
y = bigram(sourcey)

print(x)
print(y)

# 和集合
print(x | y)

# 積集合
print(x & y)

# 差集合
print(x - y)

# seというbi-gramが含まれているか
print('se' in (x | y))

# xにseが含まれているか
print('se' in x)

# yにseが含まれているか
print('se' in y)
