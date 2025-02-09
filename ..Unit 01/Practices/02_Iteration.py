# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:36:38 2025

@author: Lenovo
"""

# print ("Hello!")
# for n in range (0, 10, -2):
#    print (n)
###########      
#############    
# for x in range (2, 10, 2):
#         print (x)
# print ("Goodbye!")

# print("Hello!")
# n = 10
# while n >= 0:
#     print(n)
#     n -= 2
    

# n = 0
# while n <= 10:
#     print(n)
#     n += 2
        
###################
# T###################
# Tou can uncomment each of these examples
# and try running them yourself

# To batch comment/uncomment, select the lines and then
# on Windows hit CTRL+1 or on Mac hit CMD+1
###################



##################
# EXAMPLE: while loops 
###################
# where = input("You are in the Lost Forest. Go left or right? ")
# while where == "right":
#     where = input("You are in the Lost Forest. Go left or right? ")
# print("You got out of the Lost Forest! \o/")



###########################################

# Fun Lost Forest code, run it on your own!
#where = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
#while where.lower() == "right":
#    where = input("You are in the Lost Forest\n****************\n******       ***\n  (â•¯Â°â–¡Â°ï¼‰â•¯\n     ï¸µ \n    â”»â”â”»\n****************\n****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!\n\o/")

    
###########
## EXAMPLE    
###########
# n = int(input('Please enter a non-negative integer: '))
# while n > 0:
#     print('x')
#     n = n-1  # the same as n -= 1
    

################ YOU TRY IT ###################
## EXAMPLE: infinite loop, be careful!
# To stop it, click the shell and hit CTRL+c or 
# the red square at the top of the shell
##############################################
# while True:
#     print("noooooooo")



############### YOU TRY IT ################
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
##################
# n = 0
# where = input("Go left or right? ")
# while where == "right":
#     n = n + 1
#     if n > 2:
#         print (":(")
#     where = input("Go left or right? ")
# print("You got out!")



#############
## EXAMPLE: counter
#############

## With while loop
# n = 0
# while n < 5:
#     print(n)
#     n = n+1

## With for loop
#for n in range(5):
#    print(n)

###########
## EXAMPLE: factorial
###########

## With while loops
# x = 6
# i = 1
# factorial = 1
# while i <= x:
#     factorial *= i
#     i += 1
# print(f'{x} factorial is {factorial}')

## With for loops
# factorial = 1
# for i in range(1, x+1, 1):
#     factorial *= i
# print(f'{x} factorial is {factorial}')


# # ################ YOU TRY IT ################
# # # for i in range(1,4,1):
# # #     print(i)  
# # n = 1
# # while n <= 4:
# #     print (n)
# #     n+=1
  
# # # for j in range(1,4,2):
# # #     print(j*2)
# # n = 1
# # while n <= 4:
# #   print (n)
# #   n+=2
# # # for me in range(4,0,-1):
# # #     print("$"*me)
# # me = 4
# # while me >= 0:
# #   print ("$"*me)
# #   me -= 1


# ###########################################

# ###############
# ## EXAMPLE: sum
# ###############

# mysum = 0
# for i in range(10):
#     mysum += i
# print(mysum)

# ######

# mysum = 0
# for i in range(7, 10):
#    mysum += i
# print(mysum)

######

# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i
#     if mysum == 5:
#         break
#         mysum += 1  #wont be executed because of the breakkk
# print(mysum)

################ YOU TRY IT ################
# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 

# mysum = 0
# start = 3
# end = 5
# for i in range(start, end+1):
#     mysum += i
# print(mysum)

###########################################



#########################################################
##################### AT HOME ###########################
#########################################################

# *Practice 1:
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.
#############
# # x = 15
# # for i in range(1,x+1):
# #     if i%5 == 0:
# #         print(i)
# x = 5
#################
# for x in range (5, 16, 1):
#     if x % 5 == 0:
#         print (x)
##########
# x = 5        
# i = 5
# while i <= 15:
#     if i % 5 == 0: 
#         print (i)
#         i += 1
#     else:
#         i += 1



# *Practice 2:
# # Declare a variable n that stores an int. Print the sum of all digits 
# # in n. Hint: you can get a digit at a time looking at the remainder 
# # when you divide n by 10.
# # For ex. If x = 1234, print 10
 
# n = 10
# mysum = 0
# for n in range(10):
#     mysum =+ n
#     print (n)
    


#########################################################
##################### END AT HOME ###########################
#########################################################


#########################################################
##################### ANSWERS AT HOME ###########################
#########################################################

# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. If x = 14, it prints 5 and 10.

# x = 15
# for i in range(1,x+1):
#     if i%5 == 0:
#         print(i)


# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits 
# in n. Hint: you can get a digit at a time looking at the remainder 
# when you divide n by 10.
# For ex. If x = 1234, print 10
# n = 1234
# total = 0
# while True:
#     r = n%10
#     total += r 
#     n = n//10
#     if n == 0:
#         break
# print(total)

#########################################################
##################### END ANSWERS AT HOME ###########################
#########################################################




#########################################
############### ANSWERS TO LECTURE ##########################
#########################################
# You Try It 1: 
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
###################
# where = input("Go left or right? ")
# counter = 0
# while where == "right":
#     counter = counter + 1
#     if counter > 2:
#         print(":(")
#     where = input("Go left or right? ")
# print("You got out!")



# Your Try It 2: 
# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 

# mysum = 0
# start = 1
# end = 3
# for i in range(start, end+1):
#     mysum += i
# print(mysum)

#########################################
############### END ANSWERS TO LECTURE ##########################
#########################################
# ou can uncomment each of these examples
# and try running them yourself

# To batch comment/uncomment, select the lines and then
# on Windows hit CTRL+1 or on Mac hit CMD+1
###################



###################
# EXAMPLE: while loops 
####################
# where = input("You are in the Lost Forest. Go left or right? ")
# while where == "right":
#     where = input("You are in the Lost Forest. Go left or right? ")
# print("You got out of the Lost Forest! \o/")



###########################################

# Fun Lost Forest code, run it on your own!
#where = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
#while where.lower() == "right":
#    where = input("You are in the Lost Forest\n****************\n******       ***\n  (â•¯Â°â–¡Â°ï¼‰â•¯\n     ï¸µ \n    â”»â”â”»\n****************\n****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!\n\o/")

    
###########
## EXAMPLE    
###########
# n = int(input('Please enter a non-negative integer: '))
# while n > 0:
#     print('x')
#     n = n-1  # the same as n -= 1
    

################ YOU TRY IT ###################
## EXAMPLE: infinite loop, be careful!
# To stop it, click the shell and hit CTRL+c or 
# the red square at the top of the shell
##############################################
# while True:
#     print("noooooooo")



############### YOU TRY IT ################
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
###################
# where = input("Go left or right? ")
# while where == "right":
#     where = input("Go left or right? ")
# print("You got out!")



#############
## EXAMPLE: counter
#############

## With while loop
# n = 0
# while n < 5:
#     print(n)
#     n = n+1

## With for loop
#for n in range(5):
#    print(n)

###########
## EXAMPLE: factorial
###########

## With while loops
# x = 6
# i = 1
# factorial = 1
# while i <= x:
#     factorial *= i
#     i += 1
# print(f'{x} factorial is {factorial}')

## With for loops
# factorial = 1
# for i in range(1, x+1, 1):
#     factorial *= i
# print(f'{x} factorial is {factorial}')


################ YOU TRY IT ################
# for i in range(1,4,1):
#     print(i)
# for j in range(1,4,2):
#     print(j*2)
# for me in range(4,0,-1):
#     print("$"*me)


###########################################

###############
## EXAMPLE: sum
###############

#mysum = 0
#for i in range(10):
#    mysum += i
#print(mysum)

######

#mysum = 0
#for i in range(7, 10):
#    mysum += i
#print(mysum)

######

#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
#print(mysum)

################ YOU TRY IT ################
# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 

# mysum = 0
# start = 3
# end = 5
# for i in range(start, end):
#     mysum += i
# print(mysum)

###########################################



#########################################################
##################### AT HOME ###########################
#########################################################

# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.


# for x in range(0,15,5):
#     x += 5
#     print (x)

# x=15
# for i in range(1, x+1):
#     if i%5 == 0:
        

# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits 
# in n. Hint: you can get a digit at a time looking at the remainder 
# when you divide n by 10.
# For ex. If x = 1234, print 10
 



#########################################################
##################### END AT HOME ###########################
#########################################################


#########################################################
##################### ANSWERS AT HOME ###########################
#########################################################

# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. If x = 14, it prints 5 and 10.

# x = 15
# for i in range(1,x+1):
#     if i%5 == 0:
#         print(i)


# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits 
# in n. Hint: you can get a digit at a time looking at the remainder 
# when you divide n by 10.
# For ex. If x = 1234, print 10
# n = 1234
# total = 0
# while True:
#     r = n%10
#     total += r 
#     n = n//10
#     if n == 0:
#         break
# print(total)

# n = 123456
# total = 0
# while True:
#     r = n%10
#     total += r 
#     n = n//10
#     if n == 0:
#         break
# print(total)

# total = 0
# current = 1
# end = 6
# while current <= end:
#     total += current
#     current += 1

# print(total)

#########################################################
##################### END ANSWERS AT HOME ###########################
#########################################################



#########################################
############### ANSWERS TO LECTURE ##########################
#########################################
# You Try It 1: 
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
###################
# where = input("Go left or right? ")
# counter = 0
# while where == "right":
#     counter = counter + 1
#     if counter > 2:
#         print(":(")
#     where = input("Go left or right? ")
# print("You got out!")



# Your Try It 2: 
# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 

# mysum = 0
# start = 1
# end = 3
# for i in range(start, end+1):
#     mysum += i
# print(mysum)

#########################################
############### END ANSWERS TO LECTURE ##########################
#########################################

# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
# your program should print:Number of vowels: 5

# s = 'azcbobobegghakl'
# vowels = ["a", "e", "i", "o", "u"]
# modifiedSentence = ""
# for char in s:
#     if char in vowels:
#       modifiedSentence += char

# # print(len(modifiedSentence))
# # slength = len(modifiedSentence)
# # last = f " Number of vowels: {slength)} "
# # print (last)

# print(f'Number of vowels: {len(modifiedSentence)}')


# total = 0
# vowels ="aeiou"
# for char in s:
#     if vowels in s :
#         char += total
   


# mysum = ""
# for char in s:
#      mysum += char
#      if mysum in vowels:
#          mysum += next



# # Get user input
# sentence = input("Enter a sentence: ")
# # Define vowels
