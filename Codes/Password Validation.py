import string


def password(p):
    if len(p) < 8 or len(p) > 16: 
        return False
    flag1 = flag2 = flag3 = False
    for i in p:
        if i.isupper():
            flag1 = True
        if i.islower():
            flag2 = True
        if i in string.punctuation:
            flag3 = True
        if i.isdigit():
            flag4 = True
    if flag1 is False or flag2 is False or flag3 is False or flag4 is False:
        return False
    

print("Password must contain 8-16 characters\n1 uppercase letter, 1 lowercase letter, 1 number, 1 special character ")

p = str(input("\nEnter your new password "))
while password(p) is False:
    print("\nError")
    print("Password must contain 8-16 characters\n1 uppercase letter, 1 lowercase letter, 1 number, 1 special character ")
    p = str(input("\nRe-enter your password "))

p1 = str(input("Confirm your password "))

while p1 != p:
    print("\nError")
    p1 = str(input("Re-confirm your new password "))
print("\nSuccess")
