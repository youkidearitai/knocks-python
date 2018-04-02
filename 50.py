#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

doc = open("nlp.txt", "r").read()
words_reg = r"""
    (
        [.,;:?!]
    )
    \s
    (
        [A-Z].*
    )
"""
words = re.findall(words_reg, doc, flags=re.VERBOSE | re.MULTILINE)

if words is not None:
    for word in words:
        print(word[1])
        print("------")
