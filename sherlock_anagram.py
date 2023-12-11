#!/bin/python3

import os

def wserial(warr):
    s = ''
    for wsum in warr:
        s += str(wsum)
    return s

def sherlockAndAnagrams(s):
    found = 0
    words = {}
    wserials = {}
    for i in range(len(s)):
        word = ''
        warr = [0] * 26
        for j in range(i+1):
            word = s[i-j] + word
            warr[ord(s[i-j])-ord('a')] += 1
            if word not in words:
                serial = wserial(warr)
                words[word] = serial
                if serial not in wserials:
                    wserials[serial] = 1
                else:
                    found += wserials[serial]
                    wserials[serial] += 1
            else:
                found += wserials[words[word]]
                wserials[words[word]] += 1
    return found
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()