# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:57:29 2022

@author: nicol
src = https://youtu.be/-njsRb8Tn70
"""

import sys

chemin= r'C:\Users\nicol\OneDrive\Documents\0_Pro\software_design'
sys.path.append(chemin)

import maths as mt

ls = [1,245,4567,8,3,2,4]
print(mt.get_average([ls]))