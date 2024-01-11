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

a=int(input("enter your age"))
if a>=18:
    print("you are eligible to vote")
else:
    print("sorry you cant vote")

def vote(x):
    if x>=18:
        print("you are eligible to vote")
    else:
        print("sorry you cant vote")

vote(a)
