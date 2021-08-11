s=0
for i in range(5):
    a=int(input("Enter the marks of subject ",i+1,"out of 100:"))
    s+=a
s/=5
if(s>90):
    print("You have passed with A1 grade !")
elif(s<=90 and s>80):
    print("You have passed with A2 grade !")
elif(s<=80 and s>70):
    print("You have passed with B1 grade !")
elif(s<=70 and s>60):
    print("You have passed with B2 grade !")
elif(s<=60 and s>50):
    print("You have passed with C1 grade !")
elif(s<=50 and s>40):
    print("You have passed with C2 grade !")
else:
    print("You have failed with D grade !")
  
