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

a=[]
import random
for i in range(15):
    a.append(random.randint(1,100))
print("The unsorted array is: ",end="")
print(a)
print()
print("Bubble sort in ascending: ",end="")
print(bsortasc(a))
print()
print("Bubble sort in descending: ",end="")
print(bsortdesc(a))
print()
