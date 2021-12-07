import os,sys
import math

def converge(f,index):
    fuel = 0
    for i in range(len(f)):
        val = f[i]
        if val < index:
            fuel += sum(range(index - val +1))
        if val > index:           
            fuel += sum(range(val-index +1))
    return fuel

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    f = list(map(int,f.read().split(",")))
    delta = -1
    fuel = 0

    iterate = 0
    index = 0
    best_fuel = 10000000000

    mean = round((sum(f)/len(f)))
    index_base = 464
    best = 0

    while(iterate != 1000):

        index = index_base + iterate
        fuel_used = converge(f,index)

        if(fuel_used<best_fuel):
            best_fuel = fuel_used
            best = index

        iterate +=1

    print(best_fuel,best)
    
    
