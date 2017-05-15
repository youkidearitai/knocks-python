#!/usr/bin/env python
# -8- coding:utf-8 -*-

import wiki_03.read_wikipedia
import re

"""
[[File:City of London skyline from London City Hall - Oct 2008.jpg|thumb|250px|[[ロンドン]]
"""

media = re.compile("\[\[(?:File|ファイル):([^|]+)")
wikipedia = wiki_03.read_wikipedia.init_england_wikipedia()

for line in wikipedia.split("\n"):
    m = media.search(line)
    if m:
        print(m.group(1))
