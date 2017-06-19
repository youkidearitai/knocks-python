#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

morphs = cabocha_05.cabocha_init.cabocha_file_open()

for index in range(0, len(morphs)):
    #print("{0} -> {1}".format(index, " ".join([str(src) for src in morphs[index].srcs])))

    for src in morphs[index].srcs:
        for base_word in morphs[src].morphs:
            if base_word.pos == '動詞':
                print("{0} -> {1}".format(
                    base_word.base,
                    " ".join([dest.base for dest in morphs[index].morphs if dest.pos == '助詞'])
                ))

"""
for index in range(0, len(morphs)):
    chunk = cabocha_05.cabocha_init.verb_chunks(morphs[index], morphs)
    if chunk is not None:
        print("{0} -> {1}".format("".join([morph.surface for morph in morphs[index].morphs]), chunk))
"""
