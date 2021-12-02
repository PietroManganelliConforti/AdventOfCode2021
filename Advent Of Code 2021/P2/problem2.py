with open("input.txt") as f:
    input = f.read().splitlines()
    fow=0
    dep=0
    aim=0
    for elem in input:
        a,b = elem.split(" ")
        if(a == "forward"):
            fow+=int(b)
            dep+=int(b)*aim
        if(a == "up"):aim-=int(b)
        if(a == "down"):aim+=int(b)
    print(fow*dep)



          