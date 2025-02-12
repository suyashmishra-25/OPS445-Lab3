#!/usr/bin/env python3

'''The purpose of this script is to create a Python function that can return the free disk space on a Linux system's root directory'''

# Author ID: smishra27 / 137285227

import subprocess

def free_space():

    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", 

                            shell=True, capture_output=True, text=True)

    return result.stdout.strip()

if __name__ == '__main__':

    print(free_space())  
