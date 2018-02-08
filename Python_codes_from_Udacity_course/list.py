#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:35:38 2018

@author: nraghuva
"""

#list testing
#strings are not mutable meaning individual characters can not be changed once
#assigned
#list are mutable meaning individual element of the list can be modified



def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    sorted_list = sorted(input_list, reverse=True)
    
    return sorted_list[:3]

def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    middle_index = int(len(numbers)/2)
    
    if middle_index %2 == 0:
        return (numbers[middle_index] + numbers[middle_index -1])/2
    else:
        return numbers[middle_index]
    


list = [1,2,3,4,5,6,7,8,9]
name_list = ["Nilesh", "darshana", "Bhavna", "Jayesh"]
sample = "Nileshkumar Raghuvanshi"

#list testing
#strings are not mutable meaning individual characters can not be changed once
#assigned
#list are mutable meaning individual element of the list can be modified
""" below is an error """
#sample[5] = 'f'

""" below is not """
name_list[1] = "Darshana"


print(top_three(list))

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

#this will collect all the list element to one string plus add joining character
#to the end of each list element. joining element here is "\n"
#join works only with string and gives error when executred with datatype
#other than numbers
nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])

print(nautical_directions)

#try any other joining character here
print(" ".join(name_list))

#some more operation testing

print(min(name_list))
print(max(name_list))

print(sorted(name_list))
print(len(name_list))



