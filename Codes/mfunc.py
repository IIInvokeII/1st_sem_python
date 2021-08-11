def newmat(r,c):
    A=[[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            A[i][j]=int(input("Enter value: ")) 
    return A


def addmat(A,B):
    r1=len(A)
    c1=len(A[0])
    r2=len(B)
    c2=len(B[0])
    if(r1==r2 and c1==c2):
        mat=[[0 for i in range(c1)] for j in range(r1)]
        for i in range(r1):
            for j in range(c1):
                mat[i][j]=A[i][j]+B[i][j]
        dispmat(mat)
    else:
            print("The rows and columns of the matrices are not equal. Enter different matrices and try again")


def multimat(A,B):
    r1=len(A)
    c1=len(A[0])
    r2=len(B)
    c2=len(B[0])
    if(c1==r2):
        C=[[0 for i in range(c2)] for j in range(r1)]
        for i in range(r1):
            for j in range(r2):
                for k in range(c2):
                            C[i][j]+=A[i][k] * B[k][j]
        dispmat(C)
    else:
        print("The rows of matrix 1 and columns of matrix 2 are not of the same amount.")
        return 
        
def dispmat(A):
    r=len(A)
    c=len(A[0])
    for i in range(r):
        for j in range(c):
            print(A[i][j],end=" ")
        print()


