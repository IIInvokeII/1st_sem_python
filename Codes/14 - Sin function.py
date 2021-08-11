import f1
x=int(input("Enter the angle for x: "))
n=int(input("Enter the no. of terms: "))
c=1
sign=1
sin=0
for i in range(n):
    prev=sin
    sin=sin+sign*((x**c)/f1.fact(c))
    c+=2
    sign*=-1
    if((sin-prev)<0.0005):
        break
print("Sin",x,"=",sin)
