n=int(input("Enter the number of fibonacci numbers needed: "))
a=1
b=2
s=0
print(s)
print(a)
print(a)
print(b)
for i in range(n):
    s=a+b
    temp=a
    a=b
    b=temp+b
    print(s)

