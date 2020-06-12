#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two strings, s and t, will return the index of t as a substring of
s. Note location of a substring, t, in a string of DNA, s, is denoted
as the total number of bases, including itself, to its left.
Created on Fri Jun 12 07:31:14 2020

@author: bram
"""
from typing import List 

# Sequence and subsequence 
s = "GATATATGCATATACTTATATTT"
t = "ATAT"

# Window of length t, increases by step count of 1 and looks for match 
# each time the window is moved. If match is found, index is added 
# to list. If no match is found the wondow moves again. 
def window(string: str, substring: str) -> List:
    winSize = len(substring)
    i = iter(string)
    win = []
    
    for e in range(0, winSize):
        win.append(next(i))
    yield win
    
    for e in i:
        win = win[1:] + [e]
        print(win)
        yield win

main = window(s, t)
print(main)