# -*- coding: utf-8 -*-
"""max_min_sum_min_set_int.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/114YvOHDkzCo3m6HargEnZoWWSo6IHYAC
"""

my_list = [100,400,450,500,800,700,900,1000,200,100,400]

my_list

max(my_list)

min(my_list)

sum(my_list)

set(my_list)    #Note: Duplicate members are not displayed in sets.

my_list

for item in my_list:print(int(item)) #The output of int(my_list) will be a TypeError: int() argument must be a string, a bytes-like object, or a number, not 'list' error. #If you want to convert the numeric values in my_list to integers, you can use a for loop:

int(112.235)