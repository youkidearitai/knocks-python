#!/usr/bin/env python
# -*-coding: utf-8 -*-

import MeCab

def init():
    tagger = MeCab.Tagger("-Ochasen")
    with open("neko.txt") as fp:
        with open("neko.txt.mecab", "w") as mfp:
            mfp.write(tagger.parse(fp.read()))

if __name__ == '__main__':
    init()

