with open("dayThree.txt","r") as f:
    directions = f.read().rstrip()

santa = (0,0)
visited_houses = {santa}

for direction in directions:
    match direction:
        case "^":
            santa = (santa[0]-1,santa[1])
        case "v":
            santa = (santa[0]+1,santa[1])
        case "<":
            santa = (santa[0],santa[1]-1)
        case ">":
            santa = (santa[0],santa[1]+1)
    visited_houses.add(santa)
    
print(len(visited_houses))