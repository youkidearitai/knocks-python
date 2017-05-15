#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse(s):
    """
    冗長なほう
    """
    lists = list(s)
    ret = []
    for i in range(len(lists) - 1, -1, -1):
        ret.append(lists[i])

    return "".join(ret)


print(reverse("hoge"))
# 一行で済む方
print("hoge"[::-1])


