x=int(input("Enter a number: "))
n=int(input("Enter the no. of terms: "))
s=0
for i in range(n):
    s+=x
    x=x*10 + x
print("The computation results in: ",s)
