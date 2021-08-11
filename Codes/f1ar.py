def rfact(x):
    if(x==0):
        return 1
    else:
        return x*rfact(x-1)

def ifact(n):
    c=n
    f=1
    while(c>1):
        f*=c
        c-=1
    return f


def rfib(x):
    if(x<0):
        print("Incorrect Input")
    elif(x==1):
        return 0
    elif(x==2):
        return 1
    else:
        s=rfib(x-1)+rfib(x-2)
        return s

def  ifib(x):
    num1=-1
    num2=-1
    for i in range(x):
        fib=num1+num2
        num1=num2
        num2=fib
        print(fib)


def igcd():
    a=int(input("Enter the larger number: "))
    b=int(input("Enter the smaller number: "))
    flag=1
    for i in range(1,b+1):
        if(b%i==0 and a%i==0):
            flag=i
    print("GCD is ",flag)

def rgcd(a,b):
    if(b==0):
        return a
    else:
        return rgcd(b,a%b)

def comb(a[]):
for i in range(n):
    print('')
    print(a[i],end='')
    for j in range(n):
        if(a[j]==a[i]):
            continue
        else:
            print(a[j],end='')
    print('')
    print(a[i],end='')             
    for j in range(n-1,-1,-1):
        if(a[j]==a[i]):
            continue
        else:
            print(a[j],end='')       
    

