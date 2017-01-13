# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""

    character_list = [ c for c in text if c.isalpha() or c.isdigit() or c is ' ' ]
    word_list = "".join(character_list).lower().split()

    results = { lang['name']:len([ word for word in word_list
                                   if word in lang['common_words'] ])
                for lang in languages }

    return max(results, key=results.get)
