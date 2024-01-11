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

f=int(input("enter temperature in fahrenheit"))
c=(f-32)*(5/9)

if f< -459.67:
    print("temperature in fahrenheit can not be less than -459.67 so enter valid temperature")
else:
    print("the temperature in celsius is :",c)

def conv(x):
    c=(f-32)*(5/9)

    if x< -459.67:
        print("temperature in fahrenheit can not be less than -459.67 so enter valid temperature")
    else:
        print("the temperature in celsius is :",c)

conv(f)
