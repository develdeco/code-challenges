#!/bin/python3

import os

def isValid(s):
    chars = {}
    freqs = {}
    lenFreqs = 0
    maxFreq = 0
    
    for c in s:
        chars[c] = chars.get(c, 0) + 1
        if chars[c] not in freqs:
            freqs[chars[c]] = 1
            lenFreqs += 1
        else:
            freqs[chars[c]] += 1
            
        if chars[c] > maxFreq:
            maxFreq = chars[c]
            
        if chars[c] > 1:
            freqs[chars[c]-1] -= 1
            if freqs[chars[c]-1] == 0:
                del freqs[chars[c]-1]
                lenFreqs -= 1
                
    if lenFreqs == 1:
        return 'YES'
    elif lenFreqs == 2:
        if 1 in freqs and freqs[1] == 1:
            return 'YES'
        elif freqs[maxFreq] == 1 and maxFreq-1 in freqs:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()