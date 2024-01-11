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
if a%11==0:
    print(a," is divisible by 11")
else:
    print(a," is not divisible by 11")


def div(x):
    if x%11==0:
        print(a," is divisible by 11")
    else:
        print(a," is not divisible by 11")

div(a)