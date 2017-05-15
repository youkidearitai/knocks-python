#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json
import re

def init_england_wikipedia():
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
                return l['text']

def england_basic_specs(wikipedia):
    """
    イギリスの基礎情報のリストを返す
    """
    basic_spec = re.compile(
        r"""^\{\{基礎情報\s国\n #\sはただのスペースではなかったため
            (.+)
            ^\}\}$"""
        ,
        re.MULTILINE | re.DOTALL | re.VERBOSE
    )

    basic_spec_caption = basic_spec.search(wikipedia).group(1)
    specs = re.split(r"^\|", basic_spec_caption, flags=re.MULTILINE)

    # 下の内包表記を横に増やしすぎた
    spec_filter = lambda specs: filter(lambda sp: "=" in sp, specs)
    split_equal = lambda spec: re.split(r" *\= *", spec.rstrip())

    return {
        sp[0]: sp[1] for sp in (split_equal(spec) for spec in spec_filter(specs))
    }

def sanitize_strong(wikipedia):
    """
    強調タグを消去する

    -- wikipedia Wikipediaのmarkupされているテキスト
    """
    return re.sub(r'[\'"]+', '', wikipedia)

def sanitize_link(wikipedia):
    """
    linkタグを消去する

    -- wikipedia Wikipediaのmarkupされているテキスト
    """
    return re.sub(r"\[\[([^\]]+)\]\]", r'\1', wikipedia)

def sanitize_country_link(wikipedia):
    """
    リンクタグを消去する

    {{lang|en|United Kingdom of Great Britain and Northern Ireland}}
    -- wikipedia Wikipediaのmarkupされているテキスト
    """
    return re.sub(r'\*{0,2}\{\{lang\|(?:en|cy|ga|gd|kw|sco|fr)\|([^\}]+)\}\}', r'\1', wikipedia)

def sanitize_br_tag(wikipedia):
    """
    brタグを消去する

    -- wikipedia Wikipediaのmarkupされているテキスト
    """
    return re.sub(r'<br\s*\/?>', '', wikipedia)

def sanitize_ref_tag(wikipedia):
    """
    reftagを消去する

    -- wikipedia Wikipediaのmarkupされているテキスト
    """
    return re.sub(
        r'<ref>(.+)<\/ref>',
        r' \1',
        wikipedia,
        flags=re.MULTILINE | re.DOTALL
    )

def delete_ref_noise(wikipedia):
    """
    refタグのいらない部分を削除

    -- wikipedia Wikipediaのmarkupされているテキスト
    """

def sanitize_ref_bracket(wikipedia):
    """
    refタグのいらない部分を削除

    -- wikipedia Wikipediaのmarkupされているテキスト
    """
    return re.sub(
        r'<ref>(.+)<\/ref>',
        r' \1',
        wikipedia,
        flags=re.MULTILINE | re.DOTALL
    )

