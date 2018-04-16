#!/usr/bin/env python

"""
Print your current directory using Python.
Change into a different directory and print that one.
Create a loop that iterates over the contents of a directory and
    prints each one individually.
Create a new directory with a directory within it and another a step down.
Change the permissions of your new directory so the owner can read write
    and execute, and everyone else can only read and execute.
Delete the two subdirectories.
Use Python to create a text file that lists all of the processes that your
    user is currently running.
"""

import os

print('This is an exercise with \"os library\"!!')
print('-------------------')
print('Current Directory: ')
print('os.getcwd --> ' + os.getcwd())
print('-------------------')
print('Change into a different directory and print that one: ')
print('-------------------')
print('OLD os.getcwd --> ' + os.getcwd() )
print('<-- CHANGING os.chdir --> ')
os.chdir('/home/serrones/universe/flask_introduction')
print('NEW os.getcwd --> ' + os.getcwd() )
print('-------------------')
list_flask = os.listdir(os.getcwd())
print('List the directory\'s items: ')
[print(item) for item in list_flask]
print('-------------------')
print('Create a new directory, a directory within it and another a step down.')
os.makedirs('directory_1/directory_2/directory_3')
print('-------------------')
print('Change permissions of your new directory so the owner can read write')
os.chmod('directory_1', 755)
print('-------------------')
print('Delete the two subdirectories.')
os.chdir('/home/serrones/universe/flask_introduction/directory_1')
os.removedirs('directory_2/directory_3')
print('Deleted!')
print('-------------------')
os.chdir('/home/serrones/universe/flask_introduction')
print('-------------------')
print('Creating a text file that lists all of the processes: ')
with open('system_log', 'w') as f:
    f.write("System almost complete! We need capture the system logs")
