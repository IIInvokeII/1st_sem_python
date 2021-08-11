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


a=[76,9,233,6564,254,6,7,4,2,6,8,4,2,5,1]
print(ssortasc(a))
print(ssortdesc(a))
print("--------------------")
import bsort as b
b.bsortasc(a)
print(a)
c=a[3:]
print(c)
print("Min :",min(c))
