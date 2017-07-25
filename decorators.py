#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ribbon(func):
    ''' Decorator to put title in the middle of the ribbon. 80-chars lenght '''
    w = 80
    l = (w-2)/2 - len(func())/2
    def wrap():
        print("=" * int(l), func(), "=" * int(l))
    return wrap

def text():
    return("Text")

# use the ribbon decorator
ribbonated = ribbon(text)
ribbonated()
