n=int(input("Enter a number: "))
f=1
c=n
while(c>1):
    f*=c
    c-=1
print("The factorial of ",n,"is: ",f)
