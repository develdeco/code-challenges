# Found in code signal
def solution(a, b):
    aord = ord('a')
    src_abc = [0] * 26
    trg_abc = [0] * 26
    src_ix = []
    
    for l in a:
        src_abc[ord(l)-aord] += 1
        
    for i in range(26):
        if src_abc[i] > 0:
            src_ix.append(i)
            
    for l in b:
        trg_abc[ord(l)-aord] += 1
        
    minrep = float('inf')
    for ix in src_ix:
        rep = trg_abc[ix]//src_abc[ix]
        if rep < minrep:
            minrep = rep
            
    return minrep