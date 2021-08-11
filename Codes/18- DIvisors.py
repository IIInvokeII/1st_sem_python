n=int(input("Enter a number: "))
c=n
print("The divisors are: ")
for i in range(c):
    if(n%(i+1)==0):
        print(i+1)
