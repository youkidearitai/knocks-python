#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wiki_03.read_wikipedia
import re

wikipedia = wiki_03.read_wikipedia.init_england_wikipedia()
sections = re.compile("(==+) *([^ =]+) *(==+)")

section_list = []
for line in wikipedia.split("\n"):
    m = sections.search(line)
    if m:
        section_list.append(
            [len(m.group(1)) - 1, m.group(2)]
        )

for section in section_list:
    print("Level {0}: {1}".format(section[0], section[1]))

