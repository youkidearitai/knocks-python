#!/usr/bin/env python
# -*- coding: utf-8 -*-

string = "I am an NLPer"

# 単語bi-gram
words = string.split(" ")
bigram = [words[s:s+2] for s in range(0, len(words) - 1)]
print(bigram)

# 文字bi-gram
bigram = [string[s:s+2] for s in range(0, len(string) - 1)]
print(bigram)
