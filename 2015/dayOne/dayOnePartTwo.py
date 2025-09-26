data = open("dayOne.txt","r").read().rstrip().split()


floor = 0
up = 0
down = 0
for line in data:
    for num, letter in enumerate(line):
        if floor == -1:
            print(num)
            break
        if letter == "(":
            up+=1
            floor +=1
        elif letter == ")":
            down+= 1
            floor -=1



