#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import groupby

with open("hightemp.txt", "r") as fp:
    """
    自分が書いたすごい遅いの
    """
    col1 = {}
    # 一旦集め、数える
    for line in fp:
        sp = line.rstrip("\r\n").split("\t")
        if sp[0] in col1:
            col1[sp[0]] += 1
        else:
            col1[sp[0]] = 1

    names = col1.keys()
    values = col1.values()

    # ソートするためにdictからlistに変換
    rets = []
    for (key, value) in zip(names, values):
        rets.append([key, value])

    # 表示順に並べる
    print(sorted(rets, key=lambda value: value[1], reverse=True))

with open("hightemp.txt", "r") as fp:
    """
    itertools.groupbyを使った まとめたやつ
    """
    l = [value.split("\t")[0] for value in fp.readlines()]
    l.sort()

    prefs = [[value, len(list(group))] for value, group in groupby(l)]
    prefs.sort(key=lambda value: value[1], reverse=True)

    for pref in prefs:
        print("{0}: {1}".format(pref[0], pref[1]))

