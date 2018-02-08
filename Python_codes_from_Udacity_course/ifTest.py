#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:50:15 2018

@author: nraghuva
"""

def punctuate(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create. 
                "exclamation", "question" and "aside" are known values.
    """
    if phrase_type == "exclamation":
        sentence_punct = sentence + "!"
    elif phrase_type == "question":
        sentence_punct = sentence + "?"
    elif phrase_type == "aside":
        sentence_punct = "(" + sentence + ".)"
    else:
        sentence_punct = sentence + "."
    return sentence_punct

def punctuate2(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create. 
                "exclamation", "question" and "aside" are known values
    """
    if phrase_type == "exclamation":
        return sentence + "!"
    elif phrase_type == "question":
        return sentence + "?"
    elif phrase_type == "aside":
        return "(" + sentence + ")"
    else:
        return sentence + "."

def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        side_area += 2 * top_area
        return side_area
    else:
        return side_area



print(punctuate("Nilesh", "exclamation"))
print(punctuate2("Nilesh", "exclamation"))