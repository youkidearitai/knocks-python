#!/usr/env/bin python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

if __name__ == '__main__':
    for morph in cabocha_05.cabocha_init.cabocha_file_open()[2].morphs:
        print(
            "surface: {0} base: {1} pos: {2} pos1: {3}".format(
                morph.surface,
                morph.base,
                morph.pos,
                morph.pos1
            )
        )
