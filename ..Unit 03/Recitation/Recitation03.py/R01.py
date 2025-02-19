# 10/10 points (graded)
# Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have
# the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is
# 1*4 + 2*5 + 3*6, meaning your function should return: 32

# Hint: You will need to traverse both lists in parallel.

# This function takes in two lists of numbers and returns a number.

# def dotProduct(listA, listB):
#     '''
#     listA: a list of numbers
#     listB: a list of numbers of the same length as listA
#     '''
#     # Your code here
#*****************************************************************************************************************************************
"""
Created on Fri Feb 14 17:45:09 2025

@author: somai
Problem 1: Calculating the Dot Product of Two Lists
Explanation:
The dot product of two lists of numbers is the sum of the pairwise products of their corresponding elements. If you have two lists of equal length, such as listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is calculated as:

1*4 + 2*5 + 3*6 = 32

You will traverse both lists in parallel, multiply corresponding elements, and accumulate the results to get the final sum. This method is commonly used in linear algebra and machine learning.

Instructions:
1. Define the function dotProduct(listA, listB), which takes two lists of the same length as inputs.
2. Initialize a variable sum to 0, which will store the running total of the pairwise products.
3. Iterate through both lists using their indices (since both lists have the same length):
  - Multiply the corresponding elements from listA and listB.
  - Add the result to sum.
4. Return sum as the final result.
"""
#problem 1

#def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    Returns: the sum of the pairwise products of listA and listB
    '''
    # Initialize the sum to 0
    sum = 0
    # Traverse both lists using their indices
    for i in range(len(listA)):
        # Multiply corresponding elements and add to sum
        sum += listA[i] * listB[i]
    # Multiply corresponding elements and add to sum
    return sum 
  
def elementwise_max(listA, listB):
    """
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    Returns: a list containing the maximum of corresponding elements
    """
    result = []  # Initialize an empty list to store results
    for i in range(len(listA)):  # Iterate through indices of the lists
        result.append(max(listA[i], listB[i]))  # Append the maximum value of corresponding elements
    return result

# Test
print(elementwise_max([1, 5, 3], [4, 2, 6]))  # Output: [4, 5, 6]

  