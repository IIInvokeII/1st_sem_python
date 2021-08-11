def matadd(A,B):
    C=[[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            C[i][j]=A[i][j]+B[i][j]
    return C

def newmat():
    A=[[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            A[i][j]=int(input("Enter value: "))
    return A

def matmult(A,B):
    C=[[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j]+=A[i][k] * B[k][j]
    return C

def mattrans(A):
    C=[[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            C[j][i]=A[i][j]
    return C 

def menu():
    print("Welcome to Matrix Operations!")
    c=1

    nc=0

    names=['0','0','0','0','0']
    mat=list()

    while(c==1):
        print("")
        print("Menu: ")
        print("1. Populate New Matrix")
        print("2. Display Exising Matrix")
        print("3. Add Two Matrices")
        print("4. Multiply Two Matrices")
        print("5. Transpose a Matix")
        print("6. Exit")
    
        choice=int(input("Enter your choice: "))
    
        if(choice==1):
            print("")
            names[nc]=str(input("Enter Matrix 1's Name: "))
            mat.append(newmat())
            print("Matrix Added!")
            print(names)
            nc+=1
        
        
        elif(choice==2):
            print("")
            mname=str(input("Enter the Matrix Name: "))
            i=0
            x=1
            while(x==1):
                if(names[i]==mname):
                    print(mat[i])
                    x=0
                elif(i==4):
                    print("Matrix does not exist.")
                    x=0
                else:
                    i+=1
            
            
        elif(choice==3):
            print("")
            n1=str(input("Enter Matrix 1's Name: "))
            i=0
            x=1
            while(x==1):
                if(names[i]==n1):
                    m1=i
                    x=0
                elif(i==4):
                    print("Matrix does not exist.")
                    x=0
                else:
                    i+=1
            n2=str(input("Enter Matrix 2's Name: "))
            j=0
            y=1
            while(y==1):
                if(names[j]==n1):
                    m2=i
                    y=0
                elif(j==4):
                    print("Matrix does not exist.")
                    y=0
                else:
                    j+=1
        
            print("The sum of the matrices is: ",matadd(mat[m1],mat[m2]))

        
        elif(choice==4):
            print("")
            n1=str(input("Enter Matrix 1's Name: "))
            i=0
            x=1
            while(x==1):
                if(names[i]==n1):
                    m1=i
                    x=0
                elif(i==4):
                    print("Matrix does not exist.")
                    x=0
                else:
                    i+=1
        
            n2=str(input("Enter Matrix 2's Name: "))
            j=0
            y=1
            while(y==1):
                if(names[j]==n1):
                    m2=i
                    y=0
                elif(j==4):
                    print("Matrix does not exist.")
                    y=0
                else:
                    j+=1
            print("The product of the matrices is: ",matmult(mat[m1],mat[m2]))


        elif(choice==5):
            print("")
            n1=str(input("Enter Matrix 1's Name: "))
            i=0
            x=1
            while(x==1):
                if(names[i]==n1):
                    m1=i
                    x=0
                elif(i==4):
                    print("Matrix does not exist.")
                    x=0
                else:
                    i+=1
        
            print("The transpose of the matrix is: ",mattrans(mat[m1]))

        elif(choice==6):
            print("")
            print("Thank you for using the Matrix Functions Program!")
            c=0
        else:
            print("")
            print("Invalid option. Try again.")

        
        
        
        
    
        
