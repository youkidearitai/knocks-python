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
plt.loglog(range(1, len(values) + 1), values)
plt.show()
