#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

morphs = cabocha_05.cabocha_init.cabocha_file_open()

for index in range(0, len(morphs)):
    for morph in morphs[index].morphs:
        if morph.pos == '名詞':
            dest = cabocha_05.cabocha_init.destination(morphs[index], morphs)
            cabocha_05.cabocha_init.print_surface(dest)

