#!/usr/bin/env python
# -*-coding: utf-8 -*-

import mecab_04.mecab_init

mapping = mecab_04.mecab_init.mapping()

surfaces = [word for word in mapping if word['pos'] == '名詞' and word['pos1'] == 'サ変接続']
for surface in surfaces:
    print(surface)

