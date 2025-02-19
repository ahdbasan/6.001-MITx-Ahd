# 15/15 points (graded)
# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

# def flatten(aList):
#    '''
#    aList: a list
#    Returns a copy of aList, which is a flattened version of aList
# ***********************************************************************************************************************************
# problem 2
"""
Created on Fri Feb 14 17:45:09 2025

@author: somai
Flattening a Nested List
Explanation:
Imagine you have a list containing elements that are not only integers and strings but also other lists. Your goal is to convert this nested list into a flat list where all elements appear in a single-level list without changing their order. This process is called flattening a list.

For example, a nested list like [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5] should be flattened into [1, 'a', 'cat', 2, 3, 'dog', 4, 5].

The key challenge is that the nesting can be deep and unpredictable—you don’t know how many layers of lists there might be. Recursion is a powerful tool to handle this. Each time you encounter a sublist, you recursively flatten it until all elements are in a single-level list.

Instructions:
1. Define the function flatten(aList) that takes a nested list as input and returns a flattened version.
2. Initialize an empty list called newList to store the flattened elements.
3. Iterate through each element in the given list (aList):
  - If the element is not a list, append it directly to newList.
  - If the element is a list, recursively call flatten on that sublist and extend newList with the result.
4. Finally, return newList as the flattened list.

Example Run:

print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
# Output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

print(flatten([1, [2, [3, [4, 5]]]]))
# Output: [1, 2, 3, 4, 5]

print(flatten(['hello', ['world', ['!']]]))
# Output: ['hello', 'world', '!']
"""


def flatten(aList):
    """
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    """
    # Initialize an empty list to store the flattened elements
    newList = []
    # Iterate through each element in the list
    for elem in aList:
        # If the element is not a list, append it directly
        if not isinstance(elem, list):
            newList.append(elem)
        # If the element is a list, recursively flatten it
        else:
            newList.extend(flatten(elem))
    # Return the flattened list
    return newList


# Test cases
# print(
#     flatten([[1, "a", ["cat"], 2], [[[3]], "dog"], 4, 5])
# )  # Output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
# print(flatten([1, [2, [3, [4, 5]]]]))  # Output: [1, 2, 3, 4, 5]


def deep_reverse(aList):
    """
    aList: a nested list
    Returns a new list where the order of elements is reversed,
    and any inner lists are also reversed.
    """
    reversed_list = []
    for elem in reversed(aList):  # Reverse order of elements
        if isinstance(elem, list):
            reversed_list.append(deep_reverse(elem))  # Recursively reverse lists
        else:
            reversed_list.append(elem)
    return reversed_list


# Test cases
print(deep_reverse([[1, 2], [3, [4, 5]], 6]))  # Output: [6, [[5, 4], 3], [2, 1]]
print(deep_reverse([1, [2, [3, 4]], 5]))  # Output: [5, [[4, 3], 2], 1]


def sum_nested(aList):
    """
    aList: a nested list containing integers, strings, and other lists.
    Returns the sum of all integers in the list.
    """
    total = 0
    for elem in aList:
        if isinstance(elem, int):  # If it's an integer, add it to total
            total += elem
        elif isinstance(elem, list):  # If it's a list, recurse
            total += sum_nested(elem)
    return total


# Test cases
print(sum_nested([1, [2, [3, "a", 4]], 5]))  # Output: 15
print(sum_nested([[10, [20, 30]], ["x", [40, 50]]]))  # Output: 150


def flatten(aList):
    """Helper function to flatten a nested list"""
    newList = []
    for elem in aList:
        if isinstance(elem, list):
            newList.extend(flatten(elem))
        else:
            newList.append(elem)
    return newList


def find_max_min(aList):
    """Find maximum and minimum values in a nested list"""
    flat_list = flatten(aList)
    return max(flat_list), min(flat_list)


def count_occurrences(aList, target):
    """Count occurrences of a number in a nested list"""
    flat_list = flatten(aList)
    return flat_list.count(target)


def extract_at_depth(aList, depth, current_depth=0):
    """Extract all elements at a given depth level"""
    result = []
    if current_depth == depth:
        return aList if isinstance(aList, list) else [aList]

    if isinstance(aList, list):
        for elem in aList:
            result.extend(extract_at_depth(elem, depth, current_depth + 1))

    return result


def replace_value(aList, old_value, new_value):
    """Replace a specific value inside a nested list"""
    for i in range(len(aList)):
        if isinstance(aList[i], list):
            replace_value(aList[i], old_value, new_value)
        elif aList[i] == old_value:
            aList[i] = new_value
    return aList


def sum_nested_list(aList):
    """Find the sum of all numbers in the nested list"""
    return sum(flatten(aList))


# Given nested list
test_list = [
    [1, [2, [3, [4, [5, [6, [7, [8, 9], 10], 11], 12], 13], 14], 15], 16],
    [[[[17, 18], 19], 20], 21],
    [22, [23, [24, [25, 26], 27], 28], 29],
    [[[30, [31, 32]], 33], 34],
    35,
]

# Running all operations
print("1️ Max & Min:", find_max_min(test_list))  # (Max, Min)
print("2️ Count of 10:", count_occurrences(test_list, 10))  # Count of number 10
print("3️ Elements at depth 3:", extract_at_depth(test_list, 3))  # Extracting at depth 3
print(
    "4️ Replace 10 with 100:", replace_value(test_list, 10, 100)
)  # Replace 10 with 100
print("5️ Sum of all elements:", sum_nested_list(test_list))  # Sum of all numbers
