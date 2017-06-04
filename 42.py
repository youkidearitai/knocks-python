#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

morphs = cabocha_05.cabocha_init.cabocha_file_open()

for index in range(0, len(morphs)):
    print(
""" 文節: {0}
係り先: {1}
""".format(
            "\t".join(
                [morph.surface for morph in morphs[index].morphs if not morph.is_symbol()]
            ),
            "\t".join(
                [morph.surface for morph in morphs[morphs[index].dst].morphs if not morph.is_symbol()]
            )
        )
    )

