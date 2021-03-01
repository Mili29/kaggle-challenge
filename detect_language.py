# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:32:41 2021

@author: DELL
"""

def determine_language(item):
    import langid

    # latin my a**
    def classify(s):
        rank = langid.rank(s)
        if rank[0][0] == 'la':
            return rank[1][0]
        return rank[0][0]

    # extract text
    soup = boil_soup(item)
    for tag in ['script', 'style']:
        for el in soup.find_all(tag):
            el.extract()

    s = soup.body.text

    # determine language
    lang = classify(s)

    if lang != 'en':
        if classify(unidecode(s)) == 'en':
            return 'en'

    return lang