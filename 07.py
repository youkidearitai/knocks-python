#!/usr/bin/env python
# -*- coding: utf-8 -*-

def template(x, y, z):
    return "{0}時の{1}は{2}".format(x, y, z)

print(template("x", "y", "z"))
print(template(12, "気温", 22.4))
