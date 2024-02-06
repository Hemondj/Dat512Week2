# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:28:10 2024

@author: jimhe
"""

import sys

#file="dictionary.txt"

def load(file):
    try:
             with open(file) as in_file:
                     loaded_txt = in_file.read().strip().split('\n')
                     loaded_txt = [x.lower() for x in loaded_txt]
                     return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)