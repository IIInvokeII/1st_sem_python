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



def ssortasc(a):
    for i in range(len(a)):
        mini=i
        for j in range(i+1,len(a)):
            if(a[mini]>a[j]):
                mini=j
            a[mini],a[i]=a[i],a[mini]
    return a


def ssortdesc(a):
    for i in range(len(a)):
        mini=i
        for j in range(i+1,len(a)):
            if(a[mini]<a[j]):
                mini=j
            a[mini],a[i]=a[i],a[mini]
    return a

def lsearch(a,n):
    for i in a:
        if(i==n):
            return a.index(i)

def bsearchasc(a,n):
    l=0
    h=len(a)-1
    while(l<=h):
        m=(l+h)//2
        if(a[m]==n):
            return a.index(n)
        elif(a[m]<n):
            l=m+1
        else:
            h=m-1
    return -1

def bsearchdesc(a,n):
    h=0
    l=len(a)-1
    while(h<=l):
        m=(l+h)//2
        if(a[m]==n):
            return a.index(n)
        elif(a[m]<n):
            l=m-1
        else:
            h=m+1
    return -1

def lsearchrec(a,l,h,x):
    if(h<l):
        return -1
    if(a[l]==x):
        return l
    if(a[h]==x):
        return h
    return lsearchrec(a,l+1,h-1,x)

def bsearchrec(a,l,h,x):
    if l<=h:
        m=(l+h)//2
        if a[m]==x:
            return m
        elif a[m]<x:
            return bsearchrec(a,m+1,h,x)
        else:
            return bsearchrec(a,l,m-1,x)
    else:
        return -1

def bsearchrecd(a,l,h,x):
    if l<=h:
        m=(l+h)//2
        if a[m]==x:
            return m
        elif a[m]<x:
            return bsearchrec(a,m-1,h,x)
        else:
            return bsearchrec(a,l,m+1,x)
    else:
        return -1	

a=[76,9,233,6564,254,6,7,4,2,6,8,4,2,5,1]
print("Bubble sort in ascending: ",end="")
print(bsortasc(a))
print("Bubble sort in descending: ",end="")
print(bsortdesc(a))
print("Selection sort in ascending: ",end="")
print(ssortasc(a))
print("Selection sort in descending: ",end="")
print(ssortdesc(a))
print(bsortasc(a))
x=int(input("Enter an element to search for: "))
print("Linear search for ",x,": ")
print(lsearch(a,x))
print("Recursive linear search for ",x,": ")
print(lsearchrec(a,0,len(a)-1,x))
print("Binary search for ",x,": ")
print(bsearchasc(a,x))
bsortdesc(a)
print("Descending Binary search for ",x,": ")
print(a)
print(bsearchdesc(a,x))
bsortasc(a)
print("recursive binary search for ",x,": ")
print(a)
print(bsearchrec(a,0,len(a)-1,x))
bsortdesc(a)
print("descending recursive binary search for ",x,": ")
print(a)
print(bsearchrecd(a,len(a)-1,0,x))
