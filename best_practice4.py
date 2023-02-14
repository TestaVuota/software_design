# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:59:45 2022

@author: nicol
"""

from time import sleep
# sr : https://www.youtube.com/watch?time_continue=639&v=lOeIDvyRUQs&feature=emb_logo
print("This is my file to demonstrate best practices")

def process_data(data):
    print("Beginning data processing ...")
    modified_data = data +"Tha has been modified"
    sleep(3)
    print('Data processing finished.')
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writting data to the database")
    return print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()