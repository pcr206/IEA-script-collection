#!/usr/bin/env python3
mystring = input('Enter a string: ')
mystride = int(input('Enter a stride: '))
len_str = len(mystring)
newstr = ''
k = 0
for i in range(0, len_str, mystride):
    if (k % 2) == 0:
        newstr = newstr + mystring[i:i+mystride].upper()
    else:
        newstr = newstr + mystring[i:i+mystride].lower()

    k += 1

print(newstr)
