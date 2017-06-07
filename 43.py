#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init

morphs = cabocha_05.cabocha_init.cabocha_file_open()

for index in range(0, len(morphs)):
    dest = cabocha_05.cabocha_init.destination(morphs[index], morphs)
    if dest is not None:
        cabocha_05.cabocha_init.print_surface(dest)

