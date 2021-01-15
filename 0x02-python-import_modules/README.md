# 0x02. Python - import & modules

General
--------
Why Python programming is awesome

How to import functions from another file

How to use imported functions

How to create a module

How to use the built-in function dir()

How to prevent code in your script from being executed when imported

How to use command line arguments with your Python programs

# Requirements
General
-----------
Allowed editors: vi, vim, emacs

All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/python3

A README.md file, at the root of the folder of the project, is mandatory

Your code should use the PEP 8 style (version 1.7.*)

All your files must be executable

The length of your files will be tested using wc

Tasks 
------

###  0. Import a simple function from a simple file 
Score: 100.00% (Checks completed: 100.00%)

Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

- You have to use print function with string format to display integers
-  You have to assign:
        - the value 1 to a variable called a
        - the value 2 to a variable called b
        - and use those two variables as arguments when calling the functions add and print
- a and b must be defined in 2 different lines: a = 1 and another b = 2
- Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
- You can only use the word add_0 once in your code
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported - by using __import__, like the example below
  
  ###  1. My first toolbox! 
Score: 100.00% (Checks completed: 100.00%)

Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

- Do not use the function print (with string format to display integers) more than 4 times
- You have to define:
        - the value 10 to a variable a
        - the value 5 to a variable b
        - and use those two variables only, as arguments when calling functions (including print)
- a and b must be defined in 2 different lines: a = 10 and another b = 5
- Your program should call each of the imported functions. See example below for format
- the word calculator_1 should be used only once in your file
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

