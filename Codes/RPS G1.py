print("Welcome to Rock-Paper-Scissors!")
R=int(input("Enter the number of rounds you want to play: "))
c=1
ps=0
cs=0
import random
while(c<=R):
    print('\n')
    print("Round",c)
    a=str(input("Enter R/P/S:"))
    x=random.randint(1,3)
    if(a=='R' and x==1):
        print("Player: Rock")
        print("BOT: Rock")
        print("Draw")
        c+=1
    elif(a=='R' and x==2):
        print("Player: Rock")
        print("BOT: Paper")
        print("BOT Wins")
        cs+=1
        c+=1
    elif(a=='R' and x==3):
        print("Player: Rock")
        print("BOT: Scissors")
        print("Player Wins")
        ps+=1
        c+=1
    elif(a=='P' and x==1):
        print("Player: Paper")
        print("BOT: Rock")
        print("Players Wins")
        ps+=1
        c+=1
    elif(a=='P' and x==2):
        print("Player: Paper")
        print("BOT: Paper")
        print("Draw")
        c+=1
    elif(a=='P' and x==3):
        print("Player: Paper")
        print("BOT: Scissors")
        print("BOT Wins")
        cs+=1
        c+=1
    elif(a=='S' and x==1):
        print("Player: Scissors")
        print("BOT: Rock")
        print("BOT Wins")
        cs+=1
        c+=1
    elif(a=='S' and x==2):
        print("Player: Scissors")
        print("BOT: Paper")
        print("Player Wins")
        ps+=1
        c+=1
    elif(a=='S' and x==3):
        print("Player: Scissors")
        print("BOT: Scissors")
        print("Draw")
        c+=1
    elif(a=='exit'):
        break
    else:
        print("Invalid Option. Try again.")
print('\n')
if(ps>cs):
    print("Player Score: ",ps)
    print("BOT Score: ",cs)
    print("Player Wins!")
elif(cs>ps):
    print("Player Score: ",ps)
    print("BOT Score: ",cs)
    print("BOT Wins!")
else:
    print("Player Score: ",ps)
    print("BOT Score: ",cs)
    print("Draw!")
