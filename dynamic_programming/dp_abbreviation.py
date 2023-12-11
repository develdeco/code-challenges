#!/bin/python3

def abbreviation(a, b):
    n, m = len(a), len(b)
    M = [[False for _ in range(n+1)] for _ in range(m+1)]
    M[0][0] = True
    
    for i in range(1,n+1-m):
        if a[i-1].islower():
            M[0][i] = M[0][i-1]
        else:
            M[0][i] = False
    
    for i in range(1,m+1):
        for j in range(1,n+1+i-m):
            if a[j-1] == b[i-1]:
                M[i][j] = M[i-1][j-1]
            else:
                if a[j-1].upper() == b[i-1]:
                    M[i][j] = M[i-1][j-1] or M[i][j-1]
                elif a[j-1].islower():
                    M[i][j] = M[i][j-1]
                else:
                    M[i][j] = False

    return 'YES' if M[m][n] else 'NO'

if __name__ == '__main__':
    fptr = open('dp_abbreviation.txt', 'w')
    q = int(input().strip())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        fptr.write(result + '\n')
    fptr.close()