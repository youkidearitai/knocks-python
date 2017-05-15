#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wiki_03.read_wikipedia
import re

a = wiki_03.read_wikipedia.init_england_wikipedia()

"""
{{デフォルトソート:いきりす}}
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""

category = re.compile("Category:([^|*\]]+)")
for line in a.split("\n"):
    m = category.search(line)
    if m:
        print(line)
