# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 13:38:14 2023

@author: pierr
"""

def dec2bin(num):
    if num > 1:
        dec2bin(num // 2)
    print(num%2, end='')

dec2bin(100)