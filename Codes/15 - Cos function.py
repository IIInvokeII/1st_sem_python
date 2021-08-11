import f1
x=int(input("Enter the angle for x: "))
n=int(input("Enter the no. of terms: "))
c=0
sign=1
cos=0
for i in range(n):
    prev=cos
    cos=cos+sign*((x**c)/f1.fact(c))
    c+=2
    sign*=-1
    if((cos-prev)<0.0005):
        break
print("Cos",x,"=",cos)
