#!/usr/bin/env python
# -*-coding: utf-8 -*-

import mecab_04.mecab_init

mapping = mecab_04.mecab_init.mapping()

surfaces = [word for word in mapping if word['pos'] == '動詞']
for surface in surfaces:
    print(surface['surface'])
