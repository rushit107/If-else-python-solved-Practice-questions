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

a=int(input("enter scored percentage"))

if 60<=a<=100:
    print("You are in Division 1")
elif 45<=a<=59:
    print("you are in Divison 2")
elif 31<=a<=44:
    print("you are in Division 3")
elif 0<=a<=30:
    print("you have failed the exam")
else:
    print("enter valid percentage")

def percen(x):
    if 60<=x<=100:
        print("You are in Division 1")
    elif 45<=x<=59:
        print("you are in Divison 2")
    elif 31<=x<=44:
        print("you are in Division 3")
    elif 0<=x<=30:
        print("you have failed the exam")
    else:
        print("enter valid percentage")

percen(a)
