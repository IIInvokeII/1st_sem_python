a=[]
n=int(input("Enter the number of students: "))
print("Enter the marks of",n,"students: ")
for i in range(n):
    print("Enter the mark of student no.",i+1,":")
    a.append(int(input()))
b=tuple(a)
c=[0,0,0,0,0,0]
for i in range(n):
    if(b[i]<=100 and b[i]>90):
        c[0]+=1
    elif(b[i]<=90 and b[i]>80):
        c[1]+=1
    elif(b[i]<=80 and b[i]>70):
        c[2]+=1
    elif(b[i]<=70 and b[i]>60):
        c[3]+=1
    elif(b[i]<=60 and b[i]>50):
        c[4]+=1
    else:
        c[5]+=1
print("Statistics of the given marks are as follows: ")
print("No. of students who scored O Grade: ",c[0])
print("No. of students who scored A Grade: ",c[1])
print("No. of students who scored B Grade: ",c[2])
print("No. of students who scored C Grade: ",c[3])
print("No. of students who scored D Grade: ",c[4])
print("No. of students who scored E Grade: ",c[5])

from matplotlib import pyplot as plt
import numpy as py
x=['O','A','B','C','D','F']
y_pos=py.arange(len(x))
plt.bar(y_pos,c,align='center',alpha=0.5)
plt.xticks(y_pos,x)
plt.ylabel('No. of Students')
plt.title('Grades')
plt.show()

