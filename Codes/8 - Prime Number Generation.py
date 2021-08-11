print("PRIME NUMBER GENERATION")
l=int(input("Enter the lower limit of the range of numbers: "))
u=int(input("Enter the upper limit of the range of numbers: "))
print("The prime number in this range are: ")
while(l<=u):
    cn=0
    d=1
    while(d<=l):
        if(l%d==0):
            cn+=1
        d+=1
    if(cn<=2):
        print(l)
    l+=1

