import numpy as np
import os,sys
import math

def arr2dec(arr):
    ret = 0

    for i in range(len(arr)):
        ret += arr[i]*(2**(len(arr)-i-1))
    return ret

def splitStr(valstr):
    valstr = str(valstr)
    return [i for i in valstr] 
        

def uno_zer(input,tot_len):
    unos = np.count_nonzero(np.array(input), axis=0)
    zeros = tot_len - unos
    unos = list(unos)
    zeros = list(zeros)



with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    
    input = f.read().splitlines()
    tot_len = len(input)
    
    input = (list(map( lambda a : [int(i) for i in a] ,input )))
    print(input)
    input2test = input
    exlen = len(input[0])
    for i in range(len(input[0])):
        
        x = 0
        counter1=0
        counter0=0

        for elem in input:
            if elem[i] == 1: 
                counter1 += 1 
            else: 
                counter0 +=1

        if (counter1>=counter0) : x=1
        if (len(input) > 1 ):
            print(i,"z" ,counter0, "u",counter1)
            input = list(filter(lambda a : a[i]==x, input))
            tot_len = len(input)
            print("NEW" , input, "LEN", tot_len)
        else: break
        
    a=arr2dec(input[0])
    print(a)
    input = input2test
    print(input)
    exlen = len(input[0])
    tot_len = int(len(input))
    for i in range(len(input[0])):
        
        x = 1
        counter1=0
        counter0=0

        for elem in input:
            if elem[i] == 1: 
                counter1 += 1 
            else: 
                counter0 +=1

        if counter1>=counter0: x=0
        if counter0==0: x=1
        if (len(input) > 1 ):
            print(i, "z" ,counter0, "u", counter1, "x",x)
            input = list(filter(lambda a : a[i]==x, input))
            tot_len = len(input)
            print("NEW" , input, "LEN", tot_len)
        if (len(input) == 1 ):  break

    b = arr2dec(input[0])
    print(a*b)