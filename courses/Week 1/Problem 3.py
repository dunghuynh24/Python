""""Assume s is a string of lower case characters.

Write a program that prints the longest substring 
of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print"""
count = 0
maxcount = 0
result = 0

for char in range(len(s) - 1):
    if (s[char] <= s[char + 1]):
        count += 1
        if count > maxcount:
            maxcount = count
            result = char + 1
    else:
        count = 0
startposition = result - maxcount
print('Longest substring in alphabetical order is:', s[startposition:result + 1])