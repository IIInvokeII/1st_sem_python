print("Welcome to the 3 player Dice Game!")
name1=str(input("Enter Player 1 name: "))
name2=str(input("Enter Player 2 name: "))
name3=str(input("Ënter Player 3 name: "))
print("Are you ready ???")
print("Here we go!")
import random
s1=0
s2=0
s3=0
for c in range(10):
    s1+=random.randint(1,6)
    s2+=random.randint(1,6)
    s3+=random.randint(1,6)
print(name1,"scored",s1)
print(name2,"scored",s2)
print(name3,"scored",s3)
if(s1>s2 and s1>s3):
    print(name1,"has won the game!")
elif(s2>s1 and s2>s3):
    print(name2,"has won the game!")
elif(s3>s1 and s3>s2):
    print(name3,"has won the game!")
elif(s3>s1 and s1==s2):
    print(name3,"has won the game!")
    print("The others are drawed.")
elif(s1>s3 and s3==s2):
    print(name1,"has won the game!")
    print("The others are drawed.")
elif(s2>s1 and s1==s3):
    print(name2,"has won the game!")
    print("The others are drawed.")
elif(s2<s1 and s1==s3):
    print("The game is drawed between",name1,"and",name3)
elif(s3<s1 and s1==s2):
    print("The game is drawed between",name1,"and",name2)
elif(s1<s2 and s2==s3):
    print("The game is drawed between",name2,"and",name3)    
else:
    print("It is a draw !")
    
