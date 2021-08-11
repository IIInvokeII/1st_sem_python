n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
if(n1>n2):
    q=n1/n2
    r=n1%n2
    print("Quotient from division of",n1,"and",n2,"is",q)
    print("Remainder from division of",n1,"and",n2,"is",r)
elif(n2>n1):
    q=n2/n1
    r=n2%n1
    print("Quotient from division of",n2,"and",n1,"is",q)
    print("Remainder from division of",n2,"and",n1,"is",r)
else:
    q=n1/n2
    r=n1%n2
    print("Quotient from division of",n1,"and",n2,"is",q)
    print("Remainder from division of",n1,"and",n2,"is",r)
