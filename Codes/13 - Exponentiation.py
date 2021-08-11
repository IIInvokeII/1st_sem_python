import f1
x=int(input("Enter a value for x: "))
n=int(input("Enter no. of terms: "))
exp=0
for i in range(n):
    prev=exp
    exp+=(x**i)/f1.fact(i)
    if((exp-prev)<0.0005):
        n=0
print("The exponential of",x,"is:",exp)
