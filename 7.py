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

a=int(input("enter an year"))
if (a%400==0) or (a%100!=0 and a%4==0):
    print("it is an leap year")
else:
    print("it is not an leap year")

def leap(x):
    if (x%400==0) or (x%100!=0 and x%4==0):
        print("it is an leap year")
    else:
        print("it is not an leap year")

leap(a)