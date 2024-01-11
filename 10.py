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



#doubtSPECIALCHARACTER
a=input("enter an character:")
#b=a.isdigit()
c=a.isalpha()
d=a.isprintable()

if a.isdigit():
    print(a," is an digit")
elif c:
    print(a," is an alphabet")
elif d:
    print(a," is an special character")
else:
    print(a," is an invalid input")

def dig(x):
    b=a.isdigit()
    c=a.isalpha()
    d=a.isprintable()
    if b:
        print(a," is an digit")
    elif c:
        print(a," is an alphabet")
    elif d:
        print(a," is an special character")
    else:
        print(a," is an invalid input")


dig(a)
