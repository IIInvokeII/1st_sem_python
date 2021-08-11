n=int(input("Enter a number: "))
c=n
s=0
while(c>0):
    r=c%10
    s=s*10 + r
    c=c//10
print("The reverse of the number",n,"is",s)
if(s==n):
    print("It is a palindrome.")
else:
    print("It is not a palindrome")
