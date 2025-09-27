with open("dayThree.txt","r") as f:
    directions = f.read().rstrip()

santa = (0,0)
roboSanta = (0,0)
visited_houses = {santa}
i = 0

for direction in directions:
    i += 1
    current = santa if i%2==0 else roboSanta

    match direction:
        case "^":
            current = (current[0]-1,current[1])
        case "v":
            current = (current[0]+1,current[1])
        case "<":
            current = (current[0],current[1]-1)
        case ">":
            current = (current[0],current[1]+1)
    visited_houses.add(current)

    if i%2==0:
        santa = current
    else:
        roboSanta = current    
    
print(len(visited_houses))