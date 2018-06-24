"""Sherlock considers a string to be valid if it all characters of the string appear the same number of times.
 It is also valid if he can remove just  character at  index in the string, 
 and the remaining characters will occur the same number of times. Given a string , determine if it is valid.

For example, if , it is a valid string because frequencies are . 
So is  because we can remove one  and have  of each character in the remaining string.
 If  however, the string is not valid as we can only remove  occurrence of . That would leave character frequencies of ."""
s = 'How do you turn this on' 
a = se1t(s)
c = list(a) 
d = [s.count(c[i]) for i in range(0,len(c))]
d.sort()
#print(d)
if d[0] == d[len(c)-1]:
  print('valid1')
  
if d[0] == 1 and d[1]>1:
  if d[len(d)-1] == d[1]: 
    d.remove(min(d)) # cho ni qua phuc tap
    if d[len(c) - 1] == d[0]: # cho ni qua phuc tap
      print('valid2') # cho ni qua phuc tap
if d[0] == 1:
  if d[0] == d[len(d)-2] and d[len(d)-1] == 2:
    print('valid3')
  elif d[len(d)-2] > 1:
    print('invalid1')
  elif d[0] == d[len(d)-2] and d[len(d)-1] > 2:
    print('invalid5')

if d[0] != 1:
  if d[0] == d[len(d)-1] - 1 and d[0] == d[len(d)-2]:
    print('valid4')
  elif d[0] != d[len(c)-2]: #
    print('invalid3') 
  elif d[0] != d[len(c)-1]:
    print('invalid6')
  

    
    

