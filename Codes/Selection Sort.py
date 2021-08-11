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

print("The unsorted array is: ")
a=[]
import random
for i in range(15):
    a.append(random.randint(1,100))
print(a)
print("Selection sort in ascending: ",end="")
print(ssortasc(a))
print()
print("Selection sort in descending: ",end="")
print(ssortdesc(a))
