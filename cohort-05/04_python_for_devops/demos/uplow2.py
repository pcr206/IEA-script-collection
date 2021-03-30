#!/usr/bin/env python3
mystring = input('Enter a string: ')
mystride = int(input('Enter a stride: '))
len_str = len(mystring)
newstr = ''
k = 0
while len(mystring):
    if k  == 0:
        newstr = newstr + mystring[:mystride].upper()
        k = 1
    else:
        newstr = newstr + mystring[:mystride].lower()
        k = 0
    mystring = mystring[mystride:]


print(newstr)
