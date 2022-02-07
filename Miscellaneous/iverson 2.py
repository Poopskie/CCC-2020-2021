R = input("")
C = input("")
A = input("")


def verify(R,C,A):

    total = 0

    for i in range(len(A)):
        for j in range(len(A[i])): 
            total += A[i][j] # add up everything in that row
        
        if R[i] == total: # if the number is equal the everything in the row then continue
            total = 0
            continue
        else:
            break #if not break 
    else:
        return False #then return false

    for i in range(len(A)): #repeat the same for columns
        for j in range(len(R)):
            total += A[j][i]

        if C[i] == total:
            total = 0
            continue
        else:
            break
    else:
        return False

    return True #if it makes it through the code then it returns true



