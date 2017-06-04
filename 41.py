#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

morphs = cabocha_05.cabocha_init.cabocha_file_open()

index = 8 - 1
print(
"""文節: {0}
係り先: {1}""".format(
        ",".join([morph.surface for morph in morphs[index].morphs]),
        morphs[index].dst
    )
)

