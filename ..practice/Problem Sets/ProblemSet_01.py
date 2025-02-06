# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
# your program should print:Number of vowels: 5

s = 'azcbobobegghakl'
vowels = ["a", "e", "i", "o", "u"]
CountedVowels = ""
for char in s:
    if char in vowels:
        CountedVowels += char

print("Number of vowels:", len(CountedVowels))


# # print(len(modifiedSentence))
# # slength = len(modifiedSentence)
# # last = f " Number of vowels: {slength)} "
# # print (last)
# total = 0
# vowels ="aeiou"
# for char in s:
#     if vowels in s :
#         char += total


count = 0 
for char in s: 
    if char in vowels:
        count += 1

print(f'Number of vowels: {count}')      




###################
#THECORRECTANSWER#
vowels = "aeiou"        
count = 0        

for char in s:         
    if char in vowels:  
        count += 1     
        
print("Number of vowels:", count)           
################### 
