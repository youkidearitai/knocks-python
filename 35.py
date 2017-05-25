#!/usr/bin/env python
# -*-coding: utf-8 -*-

import mecab_04.mecab_init

mapping = mecab_04.mecab_init.mapping()

nouns = []
listnouns = []
for index in range(0, len(mapping)):
    if mapping[index]['pos'] == '名詞' and mapping[index + 1]['pos'] == '名詞':
        nouns.append(mapping[index]['surface'])
    else:
        if len(nouns) > 1:
            listnouns.append(nouns)
        nouns = []

for noun in listnouns:
    print(" ".join(noun))
