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
if a%5==0:
    print(a," is divisible by 5")
else:
    print(a," is not divisible by 5")


def div(a):
    if a%5==0:
        print(a," is divisible by 5")
    else:
        print(a," is not divisible by 5")

div(a)