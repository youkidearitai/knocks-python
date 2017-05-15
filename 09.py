#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

shuffle_strings = "My name is jessy."

def shuffle_words(shuffle_string):
    shuffle_lists = []
    words = shuffle_string.split(" ")

    for word in words:
        if len(word) > 4:
            shuffle_lists.append(
                "".join(
                    [word[0], "".join(random.sample(list(word[1:-1]), len(word[1:-1]))), word[-1]]
                )
            )
        else:
            shuffle_lists.append(word)

    return shuffle_lists

print(shuffle_words(shuffle_strings))
print(shuffle_words("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
