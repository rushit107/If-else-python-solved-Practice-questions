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
a=int(input("enter a number:"))
if a%3==0:
    print(a," is divisible by 3")
else:
    print(a," is not divisible by 3")


def div(a):
    if a%3==0:
        print(a," is divisible by 3")
    else:
        print(a," is not divisible by 3")

div(a)

