n=int(input("Enter a number: "))
c=n
s=0
while(c>0):
    r=c%10
    s=s+r**3
    c=c//10
print("The sum of the cube of the digits is",s)
if(n==s):
    print(n,"is an Amstrong number.")
else:
    print(n,"is not an Amstrong Number")
