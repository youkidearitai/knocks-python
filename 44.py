#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cabocha_05.cabocha_init
from graphviz import Digraph

morphs = cabocha_05.cabocha_init.cabocha_file_open()

G = Digraph(format="png")
G.attr('node', shape="circle")

for index in range(820, 828):
    dest = cabocha_05.cabocha_init.destination(morphs[index], morphs)

    if dest is not None:
        G.edge(
            cabocha_05.cabocha_init.merge_chunks(morphs[index]),
            cabocha_05.cabocha_init.merge_chunks(dest)
        )

G.render('binary_tree')
