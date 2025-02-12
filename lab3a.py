#!/usr/bin/env python3

'''This LAB-3a code is an example of definiton and fucntion part of python and how its used'''

# Author ID: SMISHRA27 / 137285227

def return_text_value():

    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

# return_number_value():

def return_number_value():

    num1 = 10
    num2 = 5
    return num1 + num2



# Main Program



if __name__ == '__main__':

    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))
