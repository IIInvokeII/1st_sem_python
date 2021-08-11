

result=open("python.jpg","rb")
copied=open("p.jpg","wb")

for line in result:
    copied.write(line)
result.close()
copied.close()

