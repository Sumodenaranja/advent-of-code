
pointingAt = 50
total = 0

with open("dayOne.txt","r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]

        turn = int(line[1:])
        
        if direction == "L":
            pointingAt = (pointingAt - turn)%100
        elif direction == "R":
            pointingAt = (pointingAt + turn)%100
        
        if pointingAt == 0:
            total += 1


print("The password is: " + str(total))
        