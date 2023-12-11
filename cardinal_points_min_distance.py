# Found in code signal
import math

def solution(p):
    mindis = float('inf')
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            dis = math.sqrt(pow(p[i][0]-p[j][0],2)+pow(p[i][1]-p[j][1],2))
            if dis < mindis:
                mindis = dis
    return mindis