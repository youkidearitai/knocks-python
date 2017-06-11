#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

morphs = cabocha_05.cabocha_init.cabocha_file_open()

for index in range(0, len(morphs)):
    destination = cabocha_05.cabocha_init.destination(morphs[index], morphs)
    print(
    """文節: {0}
    係り先: {1}""".format(
            ",".join([morph.surface for morph in morphs[index].morphs]),
            "\t".join([morph.surface for morph in destination.morphs])
        )
    )

