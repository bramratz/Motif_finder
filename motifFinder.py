#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two strings, s and t, will return the index of t as a substring of
s. Note location of a substring, t, in a string of DNA, s, is denoted
as the total number of bases, including itself, to its left.

Created on Fri Jun 12 07:31:14 2020

@author: bram
"""
# Import modules
from typing import List 

# Sequence and subsequence 
s = "GATATATGCATATACTTATATTT"
t = "ATAT"

# Sliding window function
def window(string: str, substring: str) -> List:
    """
    Generator. Yields window equal to the length of the substring. Each iteration moves the 
    window 1 position.
    """
    winSize = len(substring) # Size of the window
    i = iter(string) # Iterable 
    win = [] 
    
    for e in range(0, winSize):
        win.append(next(i))
    yield win
    
    for e in i:
        win = win[1:] + [e] 
        yield win

# Count the number of steps
count = 1

for w in window(s, t):
    if w == list(t):
        print(f"match at {count}") # print position of the match 
    count += 1 # Increase count 
