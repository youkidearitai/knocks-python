#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

morphs = cabocha_05.cabocha_init.cabocha_file_open()

for index in range(0, len(morphs)):
    #print("{0} -> {1}".format(index, " ".join([str(src) for src in morphs[index].srcs])))

    for base_word in morphs[index].morphs:
        if base_word.pos == '動詞':
            src_morphs = [morphs[src].morphs for src in morphs[index].srcs]
            srcs = []

            for src_morph in src_morphs:
                srcs.append([src.base for src in src_morph if src.pos == '助詞'])

            print("{0} -> {1}".format(
                base_word.base,
                " ".join([" ".join(src) for src in srcs])
            ))

"""
for index in range(0, len(morphs)):
    chunk = cabocha_05.cabocha_init.verb_chunks(morphs[index], morphs)
    if chunk is not None:
        print("{0} -> {1}".format("".join([morph.surface for morph in morphs[index].morphs]), chunk))
"""
