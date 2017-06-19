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

    def is_symbol(self):
        return self.pos == "記号"

    def is_noun(self):
        return self.pos == "名詞"


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

    def append_srcs(self, src):
        """
        係り元のインデックス番号をappendする

        - src: 係り元形態素
        """
        self.srcs.append(src)

    def append_morph(self, morph):
        """
        形態素のリストをappendする

        - morph: 係り元形態素のリスト
        """
        self.morphs.append(morph)

    def is_has_verb(self):
        """
        動詞があるかないか調べる
        """
        for morph in self.morphs:
            if morph.pos == '動詞':
                return True

        return False

    def is_has_noun(self):
        for morph in self.morphs:
            if morph.pos == '名詞':
                return True

        return False


def cabocha_file_open():
    # * 80630 -1D 0/0 0.000000
    description = re.compile("\* [0-9]+ \-?[0-9]+D [0-9]+\/[0-9]+ \-?[0-9]+(\.[0-9]+)?")
    morph_lists = []

    tmp_chunk = None

    with open("neko.txt.cabocha") as fp:
        for line in fp:
            line = line.rstrip()
            if line == "EOS":
                break

            if description.search(line) is not None:
                lists = line.split()

                if tmp_chunk is not None:
                    morph_lists.append(tmp_chunk)

                tmp_chunk = Chunk(
                    [],
                    int(lists[2].rstrip("D")),
                    []
                )

            else:
                lists = re.split("[\t,]", line)

                try:
                    tmp_chunk.append_morph(
                        Morph(
                            lists[0],
                            lists[7],
                            lists[1],
                            lists[2]
                        )
                    )
                except IndexError as indexerror:
                    raise indexerror

    for index in range(0, len(morph_lists)):
        try:
            morph_lists[morph_lists[index].dst].append_srcs(index)
        except IndexError as indexError:
            print(indexError)

    return morph_lists

def destination(morph, morphs):
    """
    係り先の文節リストを返す

    - morph: 係り元文節クラス
    - morphs: 係り先形態素のリスト
    """
    if morph.dst == -1:
        return None

    #if not morph.is_has_noun():
    #    return None

    dest = morphs[morph.dst]
    return dest

def print_surface(morph, dest):
    """
    名詞を含む文節が、動詞を含む文節を出力

    - dest 係り受け先のリスト
    """
    if dest is None:
        return

    morph_str = "".join([morph.surface for morph in morph.morphs if not morph.is_symbol()])
    dest_str = "".join([morph.surface for morph in dest.morphs if not morph.is_symbol()])

    print("{0}\t{1}".format(morph_str, dest_str))

def merge_chunks(morph):
    """
    形態素のリストのsurfaceをリストにして返す

    - morph: 形態素のリスト
    """
    return "".join(
        [morph.surface for morph in morph.morphs if not morph.is_symbol()]
    )


def verb_chunks(morph, morphs):
    """
    動詞(述語)と係り先の助詞(格)のリストを返す
    """
    dest = destination(morph, morphs)
    if dest is None:
        return []

    if not morph.is_has_verb():
        return []

    verb = None
    for src_morph in morph.morphs:
        if src_morph.pos == '動詞':
            verb = src_morph.base

    post = " ".join([dest_morph.surface for dest_morph in dest.morphs if dest_morph.pos == '助詞'])

    return "{0}\t{1}".format(verb, post)


if __name__ == '__main__':
    init()
