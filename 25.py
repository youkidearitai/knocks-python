#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wiki_03.read_wikipedia
import re

wikipedia = wiki_03.read_wikipedia.init_england_wikipedia()
spec_dicts = wiki_03.read_wikipedia.england_basic_specs(wikipedia)

for name, spec in spec_dicts.items():
    print("{0}: {1}".format(name, spec))
