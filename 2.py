#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      rushi
#
# Created:     10-01-2024
# Copyright:   (c) rushi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
d=0
if a>b:
    d=a
else:
    d=b

if d>c:
    print(d," is greater")
else:
    print(c," is greater")



def greater(x,y):
    if x>y:
        return x
    else:
        return y

A=greater(a,b)

z=greater(A,c)
print(z,"is greater")




