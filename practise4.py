ml=["car","bike","cycle"]
mll=["my ","yourv","his "]

'''ml.sort()
print(ml)
ml.reverse()
print(ml)
'''
ml1=[i+j for i,j in zip(mll,ml)]
print(ml1)
ml2=[i+j for i,j in zip(mll,ml[::-1])]
print(ml2)
l1=[1,3,4,6,3,2]
z=[]
for i in l1:
    i=i*i
    z.append(i)
print(z)
    