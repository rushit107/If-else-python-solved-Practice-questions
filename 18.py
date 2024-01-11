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

a=int(input("enter first angle"))
b=int(input("enter second angle"))
c=int(input("enter third angle"))
d=a+b+c
if d!=180:
    print("enter correct angles")
elif a==b==c:
    print("it is an equilatoral triangle")
elif a==b!=c or a==c!=b or b==c!=a:
    print("it is an isosceles triangle")
else:
    print("it is an scalar triangle")

def trianglee(p,q,r):
    d=p+q+r
    if d!=180:
        print("enter correct angles")
    elif p==q==r:
        print("it is an equilatoral triangle")
    elif p==q!=r or p==r!=q or r==p!=p:
        print("it is an isosceles triangle")
    else:
        print("it is an scalar triangle")

trianglee(a,b,c)
