#!/usr/bin/env python3



'''This function takes a single argument which is a list name itself. It will then look at the value of the last existing item in the list, it will then append a new value that is one unit bigger (i.e. +1 and modifying that same list without returning any value)'''



# Author ID: smishra27 / 137285227


# Declaring  the list before function definitions

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):

    """Appends a new item to the end of the list with the value (last item + 1)."""

    if ordered_list:  # Ensure list is not empty

        ordered_list.append(ordered_list[-1] + 1)



def remove_items_from_list(ordered_list, items_to_remove):

    """Removes all values found in items_to_remove from ordered_list."""

    for item in items_to_remove:

        while item in ordered_list:

            ordered_list.remove(item)


# Main code

if __name__ == '__main__':

    print(my_list)

    add_item_to_list(my_list)

    add_item_to_list(my_list)

    add_item_to_list(my_list)

    print(my_list)

    remove_items_from_list(my_list, [1, 5, 6])

    print(my_list)
