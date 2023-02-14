# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:59:13 2022

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

def main():
    data = "My data read from the web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

if __name__ == "__main__":
    main()