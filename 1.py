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
if a>b:
    print( a," is greater")
else:
    print(b," is greater")


def greater(x,y):
    if x>y:
        print(x," is greater")
    else:
        print(y," is greater")

greater(a,b)

print(max(a,b))












