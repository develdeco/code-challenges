#!/bin/python3

def abbreviation(a, b):
    abcap_a = [0] * 26
    ablow_a = [0] * 26
    abcap_b = [0] * 26
    ablow_b = [0] * 26
    
    aord_low = ord('a')
    aord_cap = ord('A')
    
    for c in a:
        o = ord(c)
        if o >= 97 and o <= 122:
            ablow_a[o-aord_low] += 1
        elif o >= 65 and o <= 90:
            abcap_a[o-aord_cap] += 1
        
    for c in b:
        abcap_b[ord(c)-aord_cap] += 1
        
    for i in range(26):
        ablow_b[i] = abcap_b[i] - abcap_a[i]
    
    for i in range(26):
        if ablow_a[i] < ablow_b[i] or ablow_b[i] < 0:
            return 'NO'
            
    return 'YES' 

if __name__ == '__main__':
    fptr = open('not_dp_abbreviaton.txt', 'w')
    q = int(input().strip())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        fptr.write(result + '\n')
    fptr.close()
