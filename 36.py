#!/usr/bin/env python
# -*-coding: utf-8 -*-

from itertools import groupby
import mecab_04.mecab_init

mapping = mecab_04.mecab_init.mapping()

words = [word['surface'] for word in mapping]
words.sort()

word_counts = sorted([[word, len(list(g))] for word, g in groupby(words)], reverse=True)
word_counts.sort(key=lambda data: data[1], reverse=True)
print(word_counts)

