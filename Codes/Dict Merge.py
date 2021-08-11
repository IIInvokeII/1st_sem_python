import random
l1=['a','b','c','d','e']
l2=['b','a','i','k','d']
d1={}
d2={}
for i in l1:
    d1[i]=random.randint(9000000000,9999999999)
for i in l2:
    d2[i]=random.randint(9000000000,9999999999)
print("Dictionary 1: ",end="")
print(d1)
print("Dictionary 2: ",end="")
print(d2)
d3={}
for i in d1:
    d3[i]=[d1[i]]
for i in d2:
    if i in d3:
        d3[i].append(d2[i])
    else:
        d3[i]=[d2[i]]
print("Merged Dictionary: ",end="")
print(d3)
