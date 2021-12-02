with open("input.txt") as f:
    increments = -1
    last = 0
    new = 0
    for elem in f:
        new = int(elem)
        if last < new : 
            increments+=1
        last = new
    print(increments)
