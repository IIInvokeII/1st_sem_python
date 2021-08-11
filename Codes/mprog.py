import mfunc
mat1=list()
mat2=list()
x=1
r1=0
c1=0
r2=0
c2=0
m=0
n=0

while(x==1):
    print()
    print("Welcome to Matrix Operations 2.0!")
    print("1. Enter/Modify Matrix 1")
    print("2. Enter/Modify Matrix 2")
    print("3. Display Matrix 1")
    print("4. Display Matrix 2")
    print("5. Display Sum of Existing Matrices")
    print("6. Display Product of Matrix 1 with 2")
    print("7. Display Product of Matrix 2 with 1")
    print("8. Display Transpose of Matrix 1")
    print("9. Display Transpose of Matrix 2")
    print("0. Exit")
    c=int(input("Enter your choice(0-9): "))
    if(c==1):
        r1=int(input("Enter the No. of Rows you want: "))
        c1=int(input("Enter the No. of Columns you want: "))
        mat1=mfunc.newmat(r1,c1)
        m=1
    elif(c==2):
        r2=int(input("Enter the No. of Rows you want: "))
        c2=int(input("Enter the No. of Columns you want: "))
        mat2=mfunc.newmat(r2,c2)
        n=1
    elif(c==3):
        if m==1:
            mfunc.dispmat(mat1)
        else:
            print("Matrix doesn't exist.")
    elif(c==4):
        if n==1:
            mfunc.dispmat(mat2)
        else:
            print("Matrix doesn't exist.")
    elif(c==5):
        if(m==1 and n==1):
            mfunc.addmat(mat1,mat2)
        else:
            print("No Matrix was added.")
    elif(c==6):
        if(m==1 and n==1):
            mfunc.multimat(mat1,mat2)
        else:
            print("No Matrix was added.")
    elif(c==7):
        if(m==1 and n==1):
            mfunc.multimat(mat1,mat2)
        else:
            print("No Matrix was added.")
    elif(c==8):
        if(m==1):
            mfunc.dispmat(list(zip(*mat1)))
        else:
            print("No Matrix was added.")
    elif(c==9):
        if(m==1):
            mfunc.dispmat(list(zip(*mat2)))
        else:
            print("No Matrix was added.")
    elif(c==0):
        x=0
    else:
        print("Invalid Choice, Try Again.")


