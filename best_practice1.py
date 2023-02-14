# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:21:02 2022

@author: nicol
"""

from time import sleep

print("This is my file to demonstrate best practices")

def process_data(data):
    print("Beginning data processing ...")
    modified_data = data +"Tha has been modified"
    sleep(3)
    print('Data processing finished.')
    return modified_data