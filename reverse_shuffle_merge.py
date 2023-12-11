#!/bin/python3

import math
import os
import random
import re
import sys

def checkLnum(m, lnum):
    m[lnum] -= 1
    if m[lnum] == 0:
        del m[lnum]

def reverseShuffleMerge(s):
    n = len(s)
    abcount = [0] * 26
    abpass = [0] * 26
    abcheck = [0] * 26
    wnums = {}
    aord = ord('a')
    znum = ord('z')-aord
    lnum_min = znum
    A = ''
    
    for l in s:
        abcount[ord(l)-aord] += 1/2
        
    wlen = 0
    for lnum, c in enumerate(abcount):
        if c > 0:
            wnums[lnum] = int(c)
            wlen += int(c)

    fptr.write(str(wnums)+'\n')
    pos = n-1
    pos_min = pos
    while wlen > 0:
        lnum = ord(s[pos])-aord
        lnum_first = list(wnums.keys())[0]
        if lnum == lnum_first:
            A += s[pos]
            abcheck[lnum] += 1
            checkLnum(wnums, lnum)
            lnum_min = znum
            pos_min = pos-1
            wlen -= 1
            fptr.write(A+'\n')
        else:
            if abcheck[lnum] < abcount[lnum]:
                if lnum < lnum_min:
                    lnum_min = lnum
                    pos_min = pos
                if abpass[lnum] < abcount[lnum]:
                    abpass[lnum] += 1
                else:
                    fptr.write(str(abpass)+'\n')
                    fptr.write(s[pos:pos_min+1]+'\n')
                    word = ''
                    abcheck[lnum] += 1
                    checkLnum(wnums, lnum)
                    wlen -= 1
                    lnum_min = znum
                    curr_pos = pos+1
                    old_pos = pos+1
                    lnum_max = lnum
                    warr = []
                    while curr_pos <= pos_min and wlen > 0:
                        curr_lnum = ord(s[curr_pos])-aord
                        if lnum_max >= curr_lnum:
                            if curr_lnum == lnum:
                                abpass[curr_lnum] -= 1
                                pos = curr_pos
                            elif abcheck[curr_lnum] < abcount[curr_lnum]:
                                warr.insert(0,s[curr_pos])
                                lnum_max = curr_lnum
                        curr_pos += 1
                    pos_min = pos-1
                    while old_pos < pos:
                        curr_lnum = ord(s[old_pos])-aord
                        if curr_lnum != lnum:
                            abpass[curr_lnum] -= 1
                        old_pos += 1
                    curr_pos = 0
                    while curr_pos < len(warr) and wlen > 0:
                        curr_lnum = ord(warr[curr_pos])-aord
                        if abcheck[curr_lnum] < abcount[curr_lnum]:
                            word += warr[curr_pos]
                            abcheck[curr_lnum] += 1
                            abpass[curr_lnum] -= 1
                            checkLnum(wnums, curr_lnum)
                            wlen -= 1
                            fptr.write(word+'\n')
                        curr_pos += 1
                    word += s[pos]
                    fptr.write(word+'\n')
                    A += word
                    fptr.write(A+'\n')
        pos -=1

    return A

if __name__ == '__main__':
    fptr = open('reverse_shuffle_merge.txt', 'w')
    s = input()
    fptr.write(s+'\n')
    result = reverseShuffleMerge(s)
    print(result)
    #fptr.write(result + '\n')
    fptr.close()
