a=['1','2','3','4','5','6','7','8','9']
x=0
print('---------------------------------------')
for i in range(3):
    for j in range(3):
        print ("|     ",a[x],'\t',"|",end=" ")
        x+=1
    print(' ')
    print('---------------------------------------')

c=1
print("Welcome to Tic Tac Toe 2.0!!")
while(c==1):
    print("This is a 2 player game. Player 1, do you want to be X or O?")
    s=str(input())
    t1=s
    if(t1=='O' or t1=='o'):
        t1='O'
        t2='X'
        break
    elif(t1=='X' or t1=='x' ):
        t2='O'
        t1='X'
        break
    else:
        print("Invalid option. Enter again.")
        continue

while(c<=10):
    if((a[0]=='X' and a[1]=='X' and a[2]=='X') or (a[3]=='X' and a[4]=='X' and a[5]=='X') or
       (a[6]=='X' and a[7]=='X' and a[8]=='X') or (a[0]=='X' and a[3]=='X' and a[6]=='X') or
       (a[1]=='X' and a[4]=='X' and a[7]=='X') or (a[2]=='X' and a[5]=='X' and a[8]=='X') or
       (a[2]=='X' and a[4]=='X' and a[6]=='X') or (a[0]=='X' and a[4]=='X' and a[8]=='X')):
        print("X wins!")
        break
    elif((a[0]=='O' and a[1]=='O' and a[2]=='O') or (a[3]=='O' and a[4]=='O' and a[5]=='O') or
          (a[6]=='O' and a[7]=='O' and a[8]=='O') or (a[0]=='O' and a[3]=='O' and a[6]=='O') or
          (a[1]=='O' and a[4]=='O' and a[7]=='O') or (a[2]=='O' and a[5]=='O' and a[8]=='O') or
          (a[2]=='O' and a[4]=='O' and a[6]=='O') or (a[0]=='O' and a[4]=='O' and a[8]=='O')):
        print("O wins!")
        break
    else:
        if(c==9):
            print("Draw")
            break
    if(c%2==0):
        s=t2
    else:
        s=t1
    while(c>0):
        print("Enter the position to input",s,":")
        nx=int(input())
        if(nx<1 or nx>9):
            print("Invalid position. Try again.")
        else:
            break
    a[nx-1]=s
    x=0
    print('---------------------------------------')
    for i in range(3):
        for j in range(3):
            print ("|     ",a[x],'\t',"|",end=" ")
            x+=1
        print(' ')
        print('---------------------------------------')
    c+=1

    
