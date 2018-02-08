#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:50:24 2018

@author: nraghuva
"""

# for loops

#capitalize first letter of strings
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']

for name in names:
    print(name.title())
    
def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    #number represent each member in input_list
    for number in input_list:
        sum = sum + number
    
    return sum



#These test cases check that list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))

#new
"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and ends with a right angle bracket ">".
"""
#TODO: Define the tag_count function
def tag_count(list) :
    count = 0
    
    for str in list:
        if str[0] == '<' and str[-1] == '>' :
            count +=1
    
    return count

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))

# create a new list of capitalized names without modifying the original list
capitalized_names = [] #create a new, empty list
for name in names:
    capitalized_names.append(name.title()) #add elements to the new list
    
print(capitalized_names)

"""

To create a new list we can start with an empty list ([]) and then use the append method to add new items. 
Modifying a list is a bit more involved, and requires the use of a new function: range.
 The range function takes one argument, an integer n, and returns the sequence of numbers from zero to n-1.
 >>> for number in range(4):
>>>     print(number)
0
1
2
3
We use the range function to generate the indexes for each value in the the names list. 
This lets us access the elements of the list with names[index] so that we can update the values in the names list.
"""


def html_list(str_list) :
    
    new_list = []
    new_list.append("<ul>")
    for str in str_list:
        new_list.append("<li>" + str + "</li>")
        
    new_list.append("</ul>")
    
    return "\n".join(new_list)

"""
This is our solution:

def html_list(list_items):
    HTML_string = "<ul>\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\n".format(item)
    HTML_string += "</ul>"
    return HTML_string
"""

"""
 I named the iteration variable _ to indicate that it's a dummy variable, its value isn't used in the loop body.

"""


def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box

    # print sides of box
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*") 

    print("*" * width) #print bottom edge of box
    
    
starbox(10,10)


 
