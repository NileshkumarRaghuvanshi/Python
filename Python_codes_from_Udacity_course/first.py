#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:17:52 2018

@author: nraghuva
"""
print("Jay shree Ganesh!!!")

def cylinder_volume(height, radius):
    pi = 3.14
    return pi * height * (radius ** 2)

def readable_timedelta(days):
    """Print the number of weeks and days in a number of days."""
    #to get the number of weeks we use integer division
    weeks = days // 7
    #to get the number of days that remain we use %, the modulus operator
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def print_volume(value) :
    print("The cylinder volume is {}".format(value))

return_value = print_volume(cylinder_volume(1,2))

#this return None since there is no return statement in the function
print(return_value)

print(readable_timedelta(1000))

