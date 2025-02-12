#!/usr/bin/env python3

'''The purpose of this script is to have a number of functions that return a selected number of items from a given list. Each function will return either a single item from the list OR will create a new list and return the entire new list'''

# Author ID: smishra27 / 137285227

my_list = [100, 200, 300, 'six hundred']

def give_list():

    """Returns the entire global list unchanged."""

    return my_list

def give_first_item():

    """Returns the first item of the global list as a string."""

    return str(my_list[0])

def give_first_and_last_item():

    """Returns a new list containing the first and last items."""

    return [my_list[0], my_list[-1]]



def give_second_and_third_item():

    """Returns a new list containing the second and third items."""

    return my_list[1:3]



if __name__ == '__main__':   # Main block

    print(give_list())

    print(give_first_item())

    print(give_first_and_last_item())

    print(give_second_and_third_item())


