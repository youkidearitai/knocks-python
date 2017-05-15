#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("hightemp.txt", "r") as fp:
    lists = sorted(
        [line.rstrip("\n\r").split("\t") for line in fp],
        key=lambda value: float(value[2]), reverse=True
    )

    for value in lists:
        print(
            "{0}\t{1}\t{2}\t{3}".format(
                value[0],
                value[1],
                str(value[2]),
                value[3]
            )
        )


