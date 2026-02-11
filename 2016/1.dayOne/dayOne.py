with open("dayOne.txt","r") as f:
    line = f.readline().strip()

real_address_distance = -1
positions = {"up":0,"down":0,"left":0,"right":0}
directions_map = {0:"up",90:"right",180:"down",270:"left"}
visted_positions = set((0,0))
current_coordenates = (0,0)
current_direction = 0

for instruction in map(str.strip, line.split(",")):
    direction, distance = instruction[0], int(instruction[1:])

    current_direction = (current_direction + 90 if direction == "R" else current_direction - 90) % 360
    
    if real_address_distance == -1:
        for _ in range(0,distance):
            if directions_map[current_direction] in ("right","left"):
                new_coordenates = (current_coordenates[0] + (1 if directions_map[current_direction] == "right" else -1), current_coordenates[1])
            else:
                new_coordenates = (current_coordenates[0], current_coordenates[1] + (1 if directions_map[current_direction] == "up" else -1))

            if new_coordenates in visted_positions:
                real_address_distance = abs(new_coordenates[0]) + abs(new_coordenates[1])
                break
            else:
                visted_positions.add(new_coordenates)
                current_coordenates = new_coordenates

    positions[directions_map[current_direction]] += distance

print("Part One Day One: " + str(abs(positions["left"]-positions["right"]) + abs(positions["up"]-positions["down"])))
print("Part Two Day One: " + str(real_address_distance))

