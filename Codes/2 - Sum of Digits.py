n=int(input("Enter a number: "))
c=n
s=0
while(c>0):
    r=c%10
    s=s+r
    c=c//10
print("The sum of the digits of",n,"is",s)
