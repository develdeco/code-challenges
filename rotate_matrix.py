def solution(m):
    n = len(m)
    for i in range(n//2):
        for j in range(i,n-i-1):
            temp = m[i][j]
            m[i][j] = m[n-j-1][i]
            m[n-j-1][i] = m[n-i-1][n-j-1]
            m[n-i-1][n-j-1] = m[j][n-i-1]
            m[j][n-i-1] = temp
    return m