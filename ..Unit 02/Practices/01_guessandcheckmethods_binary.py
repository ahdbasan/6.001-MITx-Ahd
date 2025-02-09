# """Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new
# string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your
# code should print out aceg."""

# s = ""
# my_str = "abcdefg"
# for i in range(0, len(my_str), 2):
#     s += my_str[i]
# print(s)


#################
## EXAMPLE: successive addition
#################

# 0.125 is a perfect power of 2
# x = 0
# for i in range(10):
#     x += 0.125
# print(x == 1.25)

#######

# 0.1 is not a perfect power of 2
# x = 0
# for i in range(10):
#     x += 0.1
# # print(x == 1)

# print(x, '==', 10*0.1)

#############
## EXAMPLE
# protip: use Python Tutor to go step-by-step: http://pythontutor.com/
#############
# *Binary representation of the decimal
# x = float(input('Enter a decimal number between 0 and 1: '))

# p = 0
# while ((2**p)*x)%1 != 0:
#     print(f'Remainder = {str((2**p)*x - int((2**p)*x))}')
#     p += 1

# num = int(x*(2**p))

# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2

# for i in range(p - len(result)):
#     result = '0' + result

# result = result[0:-p] + '.' + result[-p:]
# print(f'The binary representation of the decimal {str(x)} is {str(result)}')


################
##* EXAMPLE: Approximation by epsilon increments
## Incrementally fixing code as we find issues with approximation
################

# try with 36, 24, 2, 12345
# x = 36
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001
# while abs(guess**2 - x) >= epsilon:
#     guess += increment
#     num_guesses += 1
# print(f'num_guesses = {num_guesses}')
# print(f'{guess} is close to square root of {x}')

###########

# Caution, you'll need to "Restart Kernel" in the shell if you run this code
# x = 54321
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001
# while abs(guess**2 - x) >= epsilon:
#     guess += increment
#     num_guesses += 1
#     if num_guesses%100000 == 0:
#         print(f'Current guess = {guess}')
#         print(f'Current guess**2 - x = {abs(guess*guess - x)}')
#     if num_guesses%1000000 == 0:
#         input('continue?')
# print(f'num_guesses = {num_guesses}')
# print(f'{guess} is close to square root of {x}')

##########

# Add an extra stopping condition
# and check for why the loop terminated
# x = 54321
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001  # try with 0.00001
# while abs(guess**2 - x) >= epsilon and guess**2 <= x:
#     guess += increment
#     num_guesses += 1
# print(f'num_guesses = {num_guesses}')
# if abs(guess**2 - x) >= epsilon:
#     print(f'Failed on square root of {x}')
#     print(f'Last guess was {guess}')
#     print(f'Last guess squared is {guess*guess}')
# else:
#     print(f'{guess} is close to square root of {x}')

#######


#################################################
######################## AT HOME ##########################
#################################################
# 1. If you are incrementing from 0 by 0.022, how many increments
# can you do before you get a floating point error?

# x = 0
# count = 20     # check different numbers here
# for i in range(count):
#     x += 0.022 # increment
#     print(x)      # check this value for floating point error


# 2. Automate the code from the previous problem. Suppose you are
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself
# until you start to get a floating point error.

# your code here

#################################################
#################################################
#################################################


#################################################
################ ANSWER TO AT HOME ##########################
#################################################
# Automate the code. Suppose you are
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself
# until you start to get a floating point error.

# n = 0.022
# N = 1
# x = n
# while x == n*N:
#     print(x)
#     x += n
#     N += 1
# note that the x and N increments one extra time
# print(f'count is {N-1} where {x-n} != {n*(N-1)}')

#################################################
#################################################
#################################################


# Recall the approximation method code to find the square root
# x = 54321
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001   # try it with 0.00001
# while abs(guess**2 - x) >= epsilon and guess**2 <= x:
#     # abs(guess**2 - x) >= epsilon finds a "good enough" answer
#     # guess**2 <= x ensures we stop looking when the guess becomes unreasonable
#     guess += increment
#     num_guesses += 1
# print(f'num_guesses = {num_guesses}')

# # this "if" is for the case when we stopped the loop due to an unreasonable guess
# if abs(guess**2 - x) >= epsilon:
#     print(f'Failed on square root of {x}')
#     print(f'Last guess was {guess}')
#     print(f'Last guess squared is {guess*guess}')
# # this "else" is for the case when we stopped the loop due to being within epsilon of x
# else:
#     print(f'{guess} is close to square root of {x}')


#####################
##*EXAMPLE: fast square root using bisection search
#####################

# x = 54321  # try 0.5
# epsilon = 0.01
# num_guesses = 0
# low = 0.0
# high = x
# guess = (high + low)/2

# while abs(guess**2 - x) >= epsilon:
#     # uncomment to see each step's guess, high, and low
#     #print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     num_guesses += 1
# print(f'num_guesses = {str(num_guesses)}')
# print(f'{str(guess)} is close to square root of {str(x)}')


############### YOU TRY IT ###################
# x = 0.5
# epsilon = 0.01
# # choose the low endpoint
# low = ???
# # choose the high endpopint
# high = ???

# guess = (high + low)/2

# while abs(guess**2 - x) >= epsilon:
#     #print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# print(f'{str(guess)} is close to square root of {str(x)}')

#####################################################


#####################
## Code for square root with all x values
#####################
# x = 0.5
# epsilon = 0.01
# if x >= 1:
#    low = 1.0
#    high = x
# else:
#    low = x
#    high = 1.0
# guess = (high + low)/2
#
# while abs(guess**2 - x) >= epsilon:
#    print(f'low = {str(low)} high {str(high)} guess = {str(guess)}')
#    if guess**2 < x:
#        low = guess
#    else:
#        high = guess
#    guess = (high + low)/2.0
# print(f'{str(guess)} is close to square root of {str(x)}')


################# YOU TRY IT #######################
# Write code to use bisection search to find the cube
# root of positive cubes to within some epsilon

cube = 27
epsilon = 0.01
low = 0
high = cube

# your code here


#####################################################


######## Cube root for all cubes ############
# cube = -27
# neg = False
# if cube < 0:
#     neg = True
# cube = abs(cube)
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube :
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# if neg == True:
#     guess = -guess
# print(f'{guess} is close to the cube root of {cube}')


########################
##*EXAMPLE: Newton-Raphson to find roots
######################
# epsilon = 0.01
# k = 24  # try 54321
# guess = k/2.0
# num_guesses = 0

# while abs(guess*guess - k) >= epsilon:
#     num_guesses += 1
#     guess = guess - (((guess**2) - k)/(2*guess))
# print(f'num_guesses = {str(num_guesses)}')
# print(f'Square root of {str(k)} is about {str(guess)}')


#################################################################
################# ANSWERS TO YOU TRY IT #######################
#################################################################
# Write code to use bisection search to find the cube
# root of positive cubes to within some epsilon

# cube = 27
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube :
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     numGuesses += 1
# print('numGuesses =', numGuesses)
# print(guess, 'is close to the cube root of', cube)

#################################################################
#################################################################
#################################################################
