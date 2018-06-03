s = 'How do you turn this on' # this should be invalid, do you see it
a = set(s)
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
#if d[0] == 1 and d[1]>1:
  #if max(d) != min(d) + 1:
    #print('invalid2')
if d[0] != 1:
  if d[0] == d[len(d)-1] - 1 and d[0] == d[len(d)-2]:
    print('valid4')
  elif d[0] != d[len(c)-2]: # 
    print('invalid3') 
  elif d[0] != d[len(c)-1]:
    print('invalid6')
  

    
    
    
 # hoc cai course 2
# ok. Ko thi 2 dua them bai tap cung dc :)

