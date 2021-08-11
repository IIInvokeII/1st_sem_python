n=float(input("Enter a number: "))
d=round(n%1,10)
n=n//1
rev=0
while(n>0):
    rem=n%10
    rev=rev*10 + rem
    n=n//10
while(rev>=1):
    rev=rev/10
rev=round(rev,10)
if(d==rev):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
