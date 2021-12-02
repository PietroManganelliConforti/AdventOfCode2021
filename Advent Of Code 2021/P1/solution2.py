def compare(buf,ind):
    win1 = 0
    win2 = 0
    for i in range(3):
        win1 += buf[(ind + i)%4]
    for i in range(3):
        win2 += buf[(ind + i +1)%4]
    if win1 < win2 : return 1
    return 0 

with open("input.txt") as f:
    buffer = [0,0,0,0]  
    increments = 0 
    index = 0
    counter = 0
    for elem in f:
        buffer[counter%4] = int(elem)
        counter += 1
        if counter > 3:
            increments += compare(buffer,counter)
    print(increments)


""" 
0 - > 0 1 2 vs 1 2 3
1 - > 1 2 3 vs 2 3 4 so 1 2 3 vs 2 3 0
2 - > 2 3 4 vs 3 4 5 so 2 3 0 vs 3 0 1
3 - > 3 4 5 vs 4 5 6 

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
 """