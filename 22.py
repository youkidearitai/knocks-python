#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wiki_03.read_wikipedia
import re

wikipedia = wiki_03.read_wikipedia.init_england_wikipedia()
category = re.compile("Category:([^|*\]]+)")

for line in wikipedia.split("\n"):
    m = category.search(line)
    if m:
        print(m.group(1))
