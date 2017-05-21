#!/usr/bin/env python
# -*- coding: utf-8 -*-

mapping = []
with open('neko.txt.mecab') as fp:
    for line in fp:
        if line == 'EOS\n':
            break

        facts = line.split("\t")
        surface = facts[0]

        names = facts[1].split(",")

        mapping.append({
            'surface': surface,
            'base':    names[-2],
            'pos':     names[0],
            'pos1':    names[1]
        })


print(mapping)

