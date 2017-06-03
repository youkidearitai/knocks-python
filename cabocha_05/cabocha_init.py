#!/usr/bin/env python
# -*-coding: utf-8 -*-

import CaboCha
import re

def init():
    parser = CaboCha.Parser()
    with open("neko.txt") as fp:
        tree = parser.parse(fp.read())
        with open("neko.txt.cabocha", "w") as cfp:
            cfp.write(tree.toString(CaboCha.FORMAT_LATTICE))

class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def cabocha_file_open():
    description = re.compile("\* [0-9]+ \-?[0-9]+D [0-9]+\/[0-9]+ \-?[0-9]+(\.[0-9]+)?")
    morph_lists = []
    tmp = []

    with open("neko.txt.cabocha") as fp:
        fp.readline()

        for line in fp:
            line = line.rstrip()
            if line == "EOS":
                break

            if description.search(line) is not None:
                morph_lists.append(tmp)
                tmp = []
            else:
                lists = re.split("[\t,]", line)
                try:
                    tmp.append(
                        Morph(
                            lists[0],
                            lists[7],
                            lists[1],
                            lists[2]
                        )
                    )
                except IndexError as indexerror:
                    print(line)
                    raise indexerror

    return morph_lists

if __name__ == '__main__':
    init()
