#!/bin/python3

def minimumBribes(q):
    # Write your code here
    pos = len(q)
    totalSwaps = 0
    queue = list(range(0, len(q)+1))
    queuePos = list(range(0, len(q)+1))
    bribeCount = [0] * (len(q)+1)
    
    while pos > 0:
        swaps = pos - queuePos[q[pos-1]]
        
        if swaps < -2:
            print('Too chaotic')
            return
        
        if swaps != 0:
            direct = int(swaps/abs(swaps))
            for ix in range(queuePos[q[pos-1]], pos, direct):
                cur = queue[ix] 
                nxt = queue[ix+direct]
                
                if direct > 0:
                    if bribeCount[nxt] == 2:
                        print('Too chaotic')
                        return
                    else:
                        bribeCount[nxt] += 1
                else:
                    if bribeCount[cur] == 2:
                        print('Too chaotic')
                        return
                    else:
                        bribeCount[cur] += 1
                    
                queue[ix] = nxt
                queue[ix+direct] = cur
                queuePos[cur] = ix+direct
                queuePos[nxt] = ix
                totalSwaps += 1
            
        pos -= 1
    
    print(totalSwaps)
        

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)