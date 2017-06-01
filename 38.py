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

labels, values = zip(*counter.most_common())

plt.hist(values, bins=20, range=(0, 20))
plt.xlim(xmin=1, xmax=20)
plt.xticks(list(range(1, 20)))

plt.show()
