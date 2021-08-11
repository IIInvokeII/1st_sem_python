def bsortasc(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return a

def bsortdesc(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if(a[j]<a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=[76,9,233,6564,254,6,7,4,2,6,8,4,2,5,1]
print(bsortasc(a))
print(bsortdesc(a))
