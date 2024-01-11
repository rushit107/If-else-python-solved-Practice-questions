'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''

q=int(input("enter the quantity of product you purchased"))
if q>1000:
    c=(q*100)*(10/100)
    d=(q*100)-c
    print("HOORAY! you just got an 10% discount. please pay:",d," Rupees")
    
    
elif 1<= q <=1000:
    print("Thankyou for purchasing please pay:",q*100)
    
else:
    print("invalid quantity")