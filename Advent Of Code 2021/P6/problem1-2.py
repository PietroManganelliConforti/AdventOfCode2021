import os,sys

def evolve(test):
    for i in range(len(test)):
        if(test[i]==0):
            test[i]=6
            test.append(8)
        else:
            test[i]-=1
    return test

def evolve2(d, index):
    old = d
    new = old.copy()
    for i in range(index):
        old = new
        new = old.copy()
        for key in reversed(range(9)):
            if(key!=0):
                new[key-1]=old[key]            
            else:
                new[6] += old[0]
                new[8] = old[0]
    return new

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    input = f.read().split(",")
    #input = [3,4,3,1,2]
    d = {}
    for i in range(9):
        d[i]=0
    for elem in input:
        d[int(elem)]+=1

    #test = list(zip ( list(map(int,input)), [1 for i in range(len(input[:4])) ] ) )
   
    ret = evolve2(d, 256)
    print(ret)
    print(sum(list(ret.values())))