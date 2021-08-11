print("Welcome to Coin Toss 1.0 !")
r=str(input("Enter the reason you require a coin toss(eg. cricket, decision,etc): "))
n=int(input("Enter the number of rounds you want ot play: "))
import random
h=0
t=0
x=random.randint(1,20)
if(x%2==0):
    x=1
else:
    x=2
a=1
while(a<=n):
    print("Now choose ! Heads or Tails???? ")
    c=str(input())
    if((c=='Heads' or c=='heads' or c=='HEADS' or c=='h' or c=='H')and x==1):
        print("You have won the coin toss!")
        a+=1
        h+=1
    elif((c=='Heads' or c=='heads' or c=='HEADS' or c=='h' or c=='H')and x==2):
        print("You have lost the coin toss!")
        a+=1
    elif((c=='Tails' or c=='tails' or c=='TAILS' or c=='t' or c=='T')and x==1):
        print("You have lost the coin toss!")
        a+=1
    elif((c=='Tails' or c=='tails' or c=='TAILS' or c=='t' or c=='T')and x==2):
        print("You have won the coin toss!")
        a+=1
        t+=1
    else:
        print(c,"is not a valid choice. Please try again.")
print('\n')
print("The total tally:")
print("Heads: ",h)
print("Tails: ",t)
