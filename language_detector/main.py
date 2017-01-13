# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here

    # this variable represents how many words there are in the text for each language
    word_counter = { lang['name'] : 0 for lang in languages }

    # Remove special characters in text
    character_list = [c for c in text if c.isdigit() or c.isalpha() or c == ' ']
    word_list = "".join(character_list).split()

    for lang in languages:
        for word in word_list:
            if word in lang['common_words']:
                word_counter[lang['name']] += 1

    return max(word_counter, key=word_counter.get)
