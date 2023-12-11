import math

def solution(sizes, ustart, v):
    maxtime = max(ustart) if len(ustart) > 0 else 0
    c = [[0,[]] for _ in range(maxtime+1)]
    
    for ix, start in enumerate(ustart):
        c[start][0] += 1
        c[start][1].append(ix)
    
    ix = 0
    while ix < len(c):
        p = c[ix]
        if p[0] > 0:
            vt = v/p[0]
            minsize = float('inf')
            for i in p[1]:
                if sizes[i] < minsize:
                    minsize = sizes[i]
            
            nexttime = math.floor(ustart[p[1][0]])+1
            timeleft = nexttime - ustart[p[1][0]]
            slotneeded = False
            if vt*timeleft > minsize:
                timeleft = minsize/vt
                slotneeded = True
                
            for i in p[1]:
                sizes[i] -= vt*timeleft
                if sizes[i] > 0:
                    ustart[i] += timeleft
                    if ustart[i] > maxtime:
                        maxtime = ustart[i]
                        c.append([0,[]])
                        slotneeded = False
                    elif slotneeded:
                        c = c[:ix+1] + [[0,[]]] + c[ix+1:]
                        slotneeded = False
                    c[ix+1][0] += 1
                    c[ix+1][1].append(i)
                else:
                    ustart[i] = nexttime
        ix += 1
        
    return ustart