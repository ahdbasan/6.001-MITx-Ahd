# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:36:38 2025

@author: Lenovo
"""
# ## TYPE THIS IN THE CONSOLE -- STRINGS ##
# a = 'me'
# b = "myself"
# c = a + b
# d = a + " " + b
# silly = a * 3

# s = "abc"
# len(s) 

# ## TYPE THIS IN THE CONSOLE -- INDEXING ##
# s = "abc"
# s[0]
# s[1]
# s[2]
# #s[3]  # this is an error: type error
# s[-1]
# s[-2]
# s[-3]

# ## TYPE THIS IN THE CONSOLE -- SLICING ##
# s = "abcdefgh"
# s[3:6]
# s[3:6:2] 
# s[:]
# s[::-1] 
# s[4:1:-2]

# ## TYPE THIS IN THE CONSOLE - MANIPULATION ##
# s = "car"
# #s[0] = 'b'  # this is an error
# s = 'b'+s[1:len(s)] 


# # ## PRINTING ##
# a = "the"
# b = 3
# c = "musketeers"
# # print(a, b, c)
# # print(a + b + c)   # this is an error
# # print(a + str(b) + c)


# #########################################
# ############### ou ##########################
# #########################################


# ## *INPUT ##
# Write a program that:
# * Saves a secret number
# * Asks the user for a number guess.
# * Prints a bool depending on whether the guess matches the secret.

# # your code here
# sec_num = int (input ("guess a number   "))
# num = 10
# # if sec_num == num:
# #     print ("True")
# # else:
# #     print ("False")
# #or
# print(num == sec_num)


# ## *BRANCHING ##
# *Example 1
# pset_time = 22
# sleep_time = 8
# if (pset_time + sleep_time) > 24:
#     print("impossible!")
# elif (pset_time + sleep_time) >= 24:
#     print("full schedule!")
# else:
#     leftover = abs(24-pset_time-sleep_time)
#     print(leftover,"h of free time!")
# print("end of day")


# *Example 2
#  *Buggy, fix it!
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x,"is the same as",y)
# print("These are equal!")
#########
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x,"is the same as",y)
#     print("These are equal!")
# else:
#     print(x,"is not the same as",y)
#     print("These are not equal!")
    

# ## *NESTED BRANCHING ##
# *Practice 1
# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("therefore, x / y is", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")
# print("thanks!")


# *Practice 2
# What's printed when y = 2, y = 20, y = 11?
# What if "if x <= y:" becomes "elif x <= y:"
# answer = ''
# x = 11
# y = 2 # try 20 and 11
# if x == y:
#     answer = answer + 'M'
# if x <= y:   # try making this line: elif x <= y:
#     answer = answer + 'i'
# else:
#     answer = answer + 'T'
# print(answer)
####################
# answer = ''
# x = 11
# y = 20 # try 20 and 11
# if x == y:
#     answer = answer + 'M'
# elif x <= y:   # try making this line: elif x <= y:
#     answer = answer + 'i'
# else:
#     answer = answer + 'T'
# print(answer)


# *Practice 3
# Note that a += b is the same as a = a + b
# answer = ''
# x = 11
# # try with y = 2 and y = 12
# y = 2
# if len(str(x)) == len(str(y)):
#     if y != 0 and x%2 == 1:
#         answer = answer + "x / y is " + str(x/y)
# elif x < y:
#     answer += "\nx is smaller"  # \n inserts a newline character in the string
# else:
#     answer += "\ny is smaller"
# print(answer)
###################
# \t: Tab character
# \\: Backslash character
# \": Double quote character
# \': Single quote character
# \n: New line character
# Example with Multiple Escape Sequences:
# print("Hello\tWorld!\nThis is a \"test\".")
# Output: 
# Hello   World!
# This is a "test".
################
# answer = ''
# x = 11
# # try with y = 2 and y = 12
# y = 12
# if len(str(x)) == len(str(y)):
#     if y != 0 and x%2 == 1:
#         answer = answer + "x / y is " + str(x/y)
# elif x < y:
#     answer += "\nx is smaller"  # \n inserts a newline character in the string
# else:
#     answer += "\ny is smaller"
# print(answer)



#########################################
############### LECTURE ##########################
#########################################

# You Try It 1: Write a program that: 
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run
#########
# user = input("Enter a verb: ")
# print("I can", user, "better than you!")
# print(user, user, user, user, user)
# #or 
# print(5*user)



# You Try It 2: Write a program that:
# * Saves a secret number.
# * Asks the user for a number guess.
# * Prints whether the guess is too low, too high, or the same as the secret. 
########
# secret = 7
# guess = int(input("Guess a number between 0 and 10: "))
# if guess == secret:
#     print("You are correct.")
# elif guess < secret:
#     print("Your guess is too low.")
# else:
#     print("Your guess is too high.")

#########################################
############### END ANSWERS TO LECTURE ##########################
#########################################
num = 1
while (num < 10):
    count = 1
    while (count < 11):
        print(num, " x ", count, " = ", num*count)
        count+=1
    num+=1
    print("\n")num = 1
while (num < 10):
    count = 1
    while (count < 11):
        print(num, " x ", count, " = ", num*count)
        count+=1
    num+=1
    print("\n")
