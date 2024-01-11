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

a="aeiou"
z=a.upper()
b=input("enter  an character")
#c=b.isalpha()

if len(b)>1:
    print("please enter valid character")
elif b in a or b in z:
    print("it is an vowel")
elif not b.isalpha():
    print("enter an valid character")
else:
    print("it is an consonent")


def vow(x):
    a="aeiou"
    z=a.upper()
    c=x.isalpha()

    if len(x)>1:
        print("please enter valid character")
    elif x in a or x in z:
        print("it is an vowel")
    elif not c:
        print("entered character is not an alphabet please enter an alphabet")
    else:
        print("it is an consonent")

vow(b)

