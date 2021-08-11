import sys
score=[]

result=open("todo.txt","w")
result.write("test 93 \n")

print(result.tell())
#result.close()

#result=open("todo.txt","r")
#print(result.tell())
result.seek(0)
for line in result:
    name,sco=line.split()
    score.append(sco)

result.close()
print (score)
