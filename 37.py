#!/usr/bin/env python
# -*-coding: utf-8 -*-

import mecab_04.mecab_init
import matplotlib.pyplot as plt
import matplotlib.font_manager as fontmgr
import matplotlib

# on Mac
matplotlib.rcParams['font.family'] = 'AppleGothic'

mapping = mecab_04.mecab_init.mapping()
counter = mecab_04.mecab_init.count(mapping)

labels = [key for key, value in counter.most_common(10)]
values = [value for key, value in counter.most_common(10)]

plt.bar(
    list(range(0, 10)),
    values,
    tick_label=labels,
    align="center"
)
plt.xlabel('words')
plt.ylabel('counts')
plt.title('words of I AM A CAT')
plt.show()

