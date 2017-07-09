#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

try:
    morphs = cabocha_05.cabocha_init.cabocha_file_open()
except IndexError as ie:
    pass

for index in range(0, len(morphs)):
    dest = cabocha_05.cabocha_init.destination(morphs[index], morphs)
    if morphs[index].is_has_noun_and_verb() \
            and dest.is_has_verb():

            src_morphs = cabocha_05.cabocha_init.srcs(morphs[index].srcs, morphs)
            #print(" ".join([str(i) for i in morphs[index].srcs]))

            print("{3}: {0}{1}\t{2}".format(
                "".join([morph.surface for morph in morphs[index].morphs]),
                "".join([morph.base for morph in dest.morphs if morph.pos == '動詞']),
                " ".join([morph.surface for morph in src_morphs if morph.pos == '助詞']),
                index
            ))

