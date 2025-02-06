# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string "bob" occurs in s. 
#  For example, if s = 'azcbobobegghakl', then
# your program should print: Number of times bob occurs is: 2

# s = 'azcbobobegghakl'
# word = "bob"
# Counted = ""
# Occured = ""
# for char in s:
#     if char in word:
#         Counted += char        
# for char in Counted:
#     if char not in Occured: 
#         Occured = Occured + char
            
# print(f'Number of times bob occurs is : {len(Occured)}')

   
# # Example input string
# s = "azcbobobegghakl"

# # Initialize a counter to keep track of the number of times 'bob' appears
# count = 0

# # Loop through the string, checking every possible starting position for 'bob'
# for i in range(len(s)):  # We subtract 2 because 'bob' is 3 characters long
#     # Extract a substring of length 3 starting at position i
#     substring = s[i:i+3]
    
#     # Check if the substring is equal to 'bob'
#     if substring == "bob":
#         # If it is, increment the counter
#         count += 1

# # Print the final count of 'bob' occurrences
# print("Number of times bob occurs is:", count)

# #######################
# #THERIGHTANSWER#
# s = "azcbobobegghakl"
# count = 0
# for i in range(len(s) - 3):  
#     if s[i:i+3] == 'bob':  
#         count += 1

# print("Number of times bob occurs:", count)
# #######################



# #######################*other examples##
# s = "catcatcatdogcat"
# count = 0
# for i in range(len(s) - 2):  
#     if s[i:i+3] == 'cat':  
#         count += 1
# print("Number of times cat occurs is:", count)
# ###########################

# s = "xxxx"
# count = 0
# for i in range(len(s)- 1):  
#     if s[i:i+2] == 'xx':  
#         count += 1
# print("Number of times xx occurs is:", count)
# ###########################

# s = "banana"
# count = 0
# for i in range(len(s)- 2):  
#     if s[i:i+3] == 'ana':  
#         count += 1
# print("Number of times ana occurs is:", count)
# ##############################

# s = "aeiou"  # Example input
# vowels = "aeiou"
# count = 0

# for i in range(len(s) - 2):
#     substring = s[i:i+3]
#     if all(char in vowels for char in substring):
#         count += 1

# print("Number of vowel triplets:", count)

# ###################################


s = "baaabaaaa"  # Example input
max_streak = 0
current_streak = 0

for char in s:
    if char == 'a':
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0

print("Longest streak of 'a':", max_streak)
# #####################

# s = "running jumping swimming"  # Example input
# words = s.split()
# count = 0

# for word in words:
#     if word.endswith('ing'):
#         count += 1

# print("Number of words ending with 'ing':", count)
# #####################3

# s = "abacdc"  # Example input
# count = 0

# for i in range(len(s) - 2):
#     substring = s[i:i+3]
#     if substring == substring[::-1]:  # Check if the substring is a palindrome
#         count += 1

# print("Number of palindrome substrings:", count)
# ########################


# s = "abc123xyz"  # Example input
# count = 0

# for char in s:
#     if char.isdigit():  # Check if the character is a digit
#         count += 1

# print("Number of digits:", count)
# ##########################


# s = "abab"  # Example input
# unique_substrings = set()

# for i in range(len(s) - 1):
#     substring = s[i:i+2]
#     unique_substrings.add(substring)

# print("Number of unique substrings:", len(unique_substrings))
# ##########################
