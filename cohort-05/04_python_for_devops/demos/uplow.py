#!/usr/bin/env python3
mystring = input('Enter a string: ')
mystring = mystring.replace(' ','')
mystride = int(input('Enter a stride: '))
newstr = ''


for i in range(0,len(mystring),mystride*2):
    newstr += mystring[i:i+mystride].upper()+mystring[i+mystride:i+2*mystride].lower()

print(newstr)
