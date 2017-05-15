#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json
import re

england = re.compile('.*イギリス.*')

with gzip.open("jawiki-country.json.gz", "r") as fp:
    """
    JSONだと思ってたらJSONLだった。
    ファイルの一行ずつにJSONのObjectが乗っかっている仕様

    {'title': 'イギリス', 'text': '本文...'}
    """
    jc = [json.loads(line) for line in fp]
    for l in jc:
        if england.match(l['title']):
            print(l['text'])
            break

