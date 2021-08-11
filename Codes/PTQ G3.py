print("Welcome to Personality Test Quiz 1.0 !!")
print("Shall we begin? Press Enter.")
input()
A=0
B=0

print("Would you rather be the ")
print("A. Smartest person around")
print("B. Most charming person")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Always tell the truth")
print("B. Always lie")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Never get access to internet again")
print("B. Never get on an airplane again")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Find true love")
print("B. Win a million dollars")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Never be able to speak again")
print("B. Always speak everything on your mind")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Have a photographic memory")
print("B. Forget anything you want to")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Never be able to play your favourite game again")
print("B. Never be able to eat your favourite food again")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Be the only person in the world to live a happy life")
print("B. Be the only person in the world to live a miserable life")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Be the first person to discover a new inhabitable planet")
print("B. Be the first person to cure a very deadly disease")
x=str(input())
if(x=='A'):
    A+=1

print("Would you rather")
print("A. Be poor, and have the ability to help people")
print("B. Be rich, but only by hurting people")
x=str(input())
if(x=='A'):
    A+=1

print('\n')
print("Your results ! :")
if(A<=3):
    print("You're a pretty selfish person. Very few people would like to work with you in a team. It's not that bad though. It just means that you prefer fighting for yourself to get exactly what you want. But would you really step on other people to get there?")
elif(A>=4 and A<=6):
    print("You're a moderately selfish person. You're like the Goldilocks of this list; Not too much, not too little, just right. Most people fall into this category - You can be selfish when you need to be!")
elif(A>=7 and A<=10):
    print("You're the type of person who is always ready to sacrifice your own interests for someone else. But will you ever get what you want in life if you give it up easily for others?")
