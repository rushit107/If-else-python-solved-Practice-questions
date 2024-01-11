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

c=int(input("enter temperature in celsius"))
f=((9/5)*c)+32
if c< -273.15:
    print(" temperature in celsius can not be less than -273.15 so enter valid temperature")
else:
    print("the fahrenheit = ",f)

def conv(x):
    y=((9/5)*x)+32
    if x< -273.15:
        print(" temperature in celsius can not be less than -273.15 so enter valid temperature")
    else:
        print("the fahrenheit = ",f)

conv(c)
