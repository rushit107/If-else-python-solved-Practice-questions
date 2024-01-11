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

m=int(input("enter marks of maths"))
p=int(input("enter marks of physics"))
c=int(input("enter marks of chemistry"))
e=int(input("enter marks of english"))
h=int(input("enter marks of hindi"))

i=(m+p+c+e+h)/5

if 90<= i <=100:
    print("congratulations you have got an A grade")
elif 80<= i <=89:
    print("congratulations you have got an B grade")
elif 70<= i <=79:
    print("you have got an C grade")
elif 60<= i <=69:
    print("you have scored an D grade")
elif 40<= i <=59:
    print("you have scoed an E grade")
elif 0<= i <=39:
    print("you have faied the exam")
else:
    print("enter valid marks")


def markss(x):
    if 90<= x <=100:
        print("congratulations you have got an A grade")
    elif 80<= x <=89:
        print("congratulations you have got an B grade")
    elif 70<= x <=79:
        print("you have got an C grade")
    elif 60<= x <=69:
        print("you have scored an D grade")
    elif 40<= x <=59:
        print("you have scoed an E grade")
    elif 0<= x <=39:
        print("you have faied the exam")
    else:
        print("enter valid marks")

markss(i)
