def partitionasc(arr,low,high): 
        i = ( low-1 )
        pivot = arr[high]
        for j in range(low , high):
                if arr[j] <= pivot:
                        i = i+1
                        arr[i],arr[j] = arr[j],arr[i] 
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 )

def partitiondesc(arr,low,high): 
        i = ( low-1 )
        pivot = arr[high]
        for j in range(low , high):
                if arr[j] >= pivot:
                        i = i+1
                        arr[i],arr[j] = arr[j],arr[i] 
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 

def qsortasc(arr,low,high):
        if low < high:
                pi = partitionasc(arr,low,high)
                qsortasc(arr, low, pi-1)
                qsortasc(arr, pi+1, high)
        return arr

def qsortdesc(arr,low,high):
        if low < high:
                pi = partitiondesc(arr,low,high)
                qsortdesc(arr, low, pi-1)
                qsortdesc(arr, pi+1, high)
        return arr

a=[]
import random
for i in range(15):
    a.append(random.randint(1,100))
print("The unsorted array is: ",end="")
print(a)
print()
print("Quick sort in ascending: ",end="")
print(qsortasc(a,0,len(a)-1))
print()
print("Quick sort in descending: ",end="")
print(qsortdesc(a,0,len(a)-1))
print()
