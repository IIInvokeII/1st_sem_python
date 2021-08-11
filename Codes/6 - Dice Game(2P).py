print("Welcome to the 2 player Dice Game!")
name1=str(input("Enter Player 1 name: "))
name2=str(input("Enter Player 2 name: "))
print("Are you ready ???")
print("Here we go!")
import random
s1=0
s2=0
for c in range(10):
    s1+=random.randint(1,6)
    s2+=random.randint(1,6)
print(name1,"scored",s1)
print(name2,"scored",s2)
if(s1>s2):
    print(name1,"has won the game!")
elif(s2>s1):
    print(name2,"has won the game!")
else:
    print("It is a draw !")
    
