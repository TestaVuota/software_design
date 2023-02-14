# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:49:53 2022

@author: nicol
"""
"""
src = https://youtu.be/-njsRb8Tn70
"""
"""
list of functions
"""

def get_max(lst):
    mx = float ("-inf")
    
    for num in lst:
        if num in lst:
            if num > mx:
                mx = num
    return mx


def get_min(lst):
    mn = float ("-inf")
    
    for num in lst:
        if num in lst:
            if num > mn:
                mn = num
    return mn

def get_average(lst):
    return sum(lst)/len(lst)

def get_median(lst):
    lst = sorted(lst)
    
    if len(lst) %2 == 0:
        return (lst[len(lst)/2 - 1] - lst[len(lst)/2])
    
    else:
        return lst[(len(lst) - 1)/2]