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
    """
    形態素を表すクラス

    - surface 表層形
    - base 基本型
    - pos 品詞
    - pos1 品詞細分類1
    """
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk(object):
    """
    文節を表すクラス

    - morphs 形態素のリスト(Morph)
    - dst 係り先文節インデックス番号
    - srcs 係り元文節インデックスのリスト
    """
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

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
                lists = line.split()
                morph_lists.append(
                    Chunk(
                        tmp,
                        int(lists[2].rstrip("D")),
                        int(lists[1])
                    )
                )
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
