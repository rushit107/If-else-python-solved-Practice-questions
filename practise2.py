'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''

q=int(input("enter the no. of classes you attended:"))
r=30
p=(q*100)/r
if 0 < p > 100:
    print("please enter valid entry")
elif p<75:
    print("sorry! you cant attend exam")
else:
    print("you can attend exam")