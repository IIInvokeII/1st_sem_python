n=int(input("Enter a number: "))
c=n
s=0
d=0
while(c>=1):
    c=c/10
    d+=1
c=n
while(c>0):
    r=c%10
    s=s+r**d
    c=c//10
print("The sum of the digits to the power",d,"is: ",s)
if(n==s):
    print(n,"is an Armstrong number.")
else:
    print(n,"is not an Armstrong Number")

