#!/usr/bin/env python
# -*-coding: utf-8 -*-

import mecab_04.mecab_init

mapping = mecab_04.mecab_init.mapping()

for index in range(0, len(mapping)):
    if mapping[index]['surface'] == 'の' and \
            mapping[index - 1]['pos'] == '名詞' and \
            mapping[index + 1]['pos'] == '名詞':
        print(
            "{0} {1} {2}".format(
                mapping[index - 1]['surface'],
                mapping[index]['surface'],
                mapping[index + 1]['surface']
            )
        )

