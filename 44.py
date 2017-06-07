#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init
from graphviz import Digraph

morphs = cabocha_05.cabocha_init.cabocha_file_open()

G = Digraph(format="png")
G.attr('node', shape="circle")

for index in range(10, 104):
    dest = cabocha_05.cabocha_init.destination(morphs[index], morphs)
    if dest is not None:
        for d in dest.morphs:
            for morph in morphs[index].morphs:
                G.edge(morph.surface, d.surface)

G.render('binary_tree')
