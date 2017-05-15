#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(words):
    """
    暗号化・復号化するメソッド
    ASCIIコードに則っている

    words 暗号化・復号化するメソッド
    """
    ret = ''
    for i in range(0, len(words)):
        ascii_code = ord(words[i])

        # asciiコードで[a-z] (英小文字)なら
        if ascii_code >= ord('a') and ascii_code <= ord('z'):
            ret += chr(219 - ascii_code)
        else:
            ret += words[i]

    return ret

def cipher_oneline(words):
    return "".join(
        [
            chr(
                219 - ord(word) if word.islower() else ord(word)
            )
            for word in words
        ]
    )

words = "Hhoge"

print(cipher(words))
print(cipher(cipher(words)))

print(cipher_oneline(words))
print(cipher_oneline(cipher_oneline(words)))
