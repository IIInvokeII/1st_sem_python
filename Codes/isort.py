def isortasc(a):
        for i in range(1,len(a)):
                key=a[i]
                j=i-1
                while(j>=0 and key<a[j]):
                        a[j+1]=a[j]
                        j-=1
                a[j+1]=key
        return a

def isortdesc(a):
        for i in range(1,len(a)):
                key=a[i]
                j=i-1
                while(j>=0 and key>a[j]):
                        a[j+1]=a[j]
                        j-=1
                a[j+1]=key
        return a
                
a=[]
import random
for i in range(15):
    a.append(random.randint(1,100))
print("The unsorted array is: ",end="")
print(a)
print()
print("Insertion sort in ascending: ",end="")
print(isortasc(a))
print()
print("Insertion sort in descending: ",end="")
print(isortdesc(a))
print()


