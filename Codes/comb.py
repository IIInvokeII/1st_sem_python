import f1ar
print("Enter a number: ")
a=list(input())
n=len(a)
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
