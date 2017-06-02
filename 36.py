#!/usr/bin/env python
# -*-coding: utf-8 -*-

import mecab_04.mecab_init

mapping = mecab_04.mecab_init.mapping()
counter = mecab_04.mecab_init.count(mapping)

for (key, value) in counter.most_common():
    print("{0}: {1}".format(key, value))
