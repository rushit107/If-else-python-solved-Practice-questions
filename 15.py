#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rushi
#
# Created:     10-01-2024
# Copyright:   (c) rushi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=input("please enter an character")
x=a.isupper()
y=a.islower()

if x:
    print(a," is uppercase")
elif y:
    print(a," is lowercase")
else:
    print("entered character is neither uppercase nor lowercase")


def case(s):
    x=s.isupper()
    y=s.islower()

    if x:
        print(s," is uppercase")
    elif y:
        print(s," is lowercase")
    else:
        print("entered character is neither uppercase nor lowercase")

case(a)

