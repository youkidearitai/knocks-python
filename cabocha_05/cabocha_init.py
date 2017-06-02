#!/usr/bin/env python
# -*-coding: utf-8 -*-

import CaboCha

def init():
    parser = CaboCha.Parser()
    with open("neko.txt") as fp:
        tree = parser.parse(fp.read())
        with open("neko.txt.cabocha", "w") as cfp:
            cfp.write(tree.toString(CaboCha.FORMAT_LATTICE))

if __name__ == '__main__':
    init()
