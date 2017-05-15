#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wiki_03.read_wikipedia

wikipedia = wiki_03.read_wikipedia.init_england_wikipedia()
basic_specs = wiki_03.read_wikipedia.england_basic_specs(wikipedia)

for name, spec in basic_specs.items():
    print(
        "{0}: {1}".format(
            name,
            wiki_03.read_wikipedia.sanitize_link(
                wiki_03.read_wikipedia.sanitize_strong(
                    wiki_03.read_wikipedia.sanitize_br_tag(
                        wiki_03.read_wikipedia.sanitize_country_link(
                            wiki_03.read_wikipedia.sanitize_ref_tag(
                                spec
                            )
                        )
                    )
                )
            )
        )
    )
