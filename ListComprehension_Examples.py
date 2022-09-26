# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:03:52 2022

@author: Vincent Medrano
"""

myList = [1,2,3,4,5]
# multiply every item in list by 2
print([2*item for item in myList])

# creates a list from 0 to 99
my_second_list = list(range(100))
# if number % 10 has no remainder, then add to filteredList
filteredList = [item for item in my_second_list if item % 10 == 0]
print(filteredList)

# add number to list if remainder is less than 3 (will return numbers
# that end in 0, 1 and 2)
filteredList = [item for item in my_second_list if item % 10 < 3]
print(filteredList)


myString = "My name is Vincent. I live in Lake Los Angeles."
# split the string at the period
print(myString.split("."))
# split everything that has a space after
print(myString.split())
# Removes periods and converts words to lower case
def cleanUp(word):
    return word.replace(".", "").lower()

print([cleanUp(word) for word in myString.split()])

# grab all words less than 3 characters long
print([cleanUp(word) for word in myString.split() if len(cleanUp(word)) < 3])

# create a list of list that break at the period using nested list comprehension
print([[cleanUp(word) for word in sentence.split()] for sentence in myString.split(".")])



