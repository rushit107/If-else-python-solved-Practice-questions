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

a=["january","march","may","july","august","october","december"]

b=["february","april","june","september","november"]

d=["february"]

z=input("enter an month")
c=z.lower()

if c in a:
    print("there are 31 days in ",c)
elif c in b and c in d:
    print("there are 30 days in ",c ,"but if it is leap year than it consists 29 days")
elif c in b:
    print("there are 30 days in ",c)
else:
    print("enter valid month")

def month(x):
    c=x.lower()

    if c in a:
        print("there are 31 days in ",c)
    elif c in b and c in d:
        print("there are 30 days in ",c ,"but if it is leap year than it consists 29 days")
    elif c in b:
        print("there are 30 days in ",c)
    else:
        print("enter valid month")

month(z)
