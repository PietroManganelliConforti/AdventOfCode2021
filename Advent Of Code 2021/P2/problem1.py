with open("input.txt") as f:
    input = f.read().splitlines()
    fow=0
    dep=0
    for elem in input:
        a,b = elem.split(" ")
        if(a == "forward"):fow+=int(b)
        if(a == "up"):dep-=int(b)
        if(a == "down"):dep+=int(b)
    print(fow*dep)



          
       