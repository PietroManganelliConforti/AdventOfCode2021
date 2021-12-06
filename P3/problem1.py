import numpy as np
import os,sys

def arr2dec(arr):
    ret = 0
    for i in range(len(arr)):
        ret += arr[i]*(2**(11-i))
    return ret

def splitStr(valstr):
    valstr = str(valstr)
    return [i for i in valstr] 
        

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    input = f.read().splitlines()
    tot_len = len(input)
    input = np.array(list(map( lambda a : [int(i) for i in a] ,input )))
    print(input)
    unos = np.count_nonzero(input, axis=0)
    print(unos)
    zeros = tot_len - unos
    print(zeros)

    unos = list(unos)
    zeros = list(zeros)

    c1 = [ 1 if unos[i]>tot_len/2 else 0  for i in range(len(unos))]
    c2 = [1 - i for i in c1 ]

    print(arr2dec(c1)*arr2dec(c2))

