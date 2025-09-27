import numpy as np
import pandas as pd
import time

# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

super_start_time = time.time()

directions = {
    0:"up",
    1:"right",
    2:"down",
    3:"left"
}

pathfile = "daySix.txt"
pointingDirection = 0
tilesChecked = 0

def in_bounds(position,direction):
    pointing = directions[int((direction % 360) // 90)]
    
    if pointing == "up" and int(position[0]) <= 0:
        return False
    elif pointing == "right" and int(position[1]) >= 129:
        return False
    elif pointing == "down" and int(position[0]) >= 129:
        return False
    elif pointing == "left" and int(position[1]) <= 0:
        return False
    else:
        return True




with open(pathfile,"r") as f:
    lines = [line.strip() for line in f]

grid = [list(character) for character in lines]

arr = np.array(grid)

guard = tuple(idx[0] for idx in np.where(arr == "^")) # y,x

start_time = time.time()

while in_bounds(guard,pointingDirection):

    if arr[guard] != "X":
        tilesChecked += 1
        arr[guard] = "X"
    
    pointing = directions[(pointingDirection % 360) // 90]

    if pointing == "up" and in_bounds((guard[0] -1, guard[1]),pointingDirection):
        if arr[guard[0] -1, guard[1]] == "#":
            pointingDirection += 90
        else:
            guard = (guard[0] - 1, guard[1])
        
    elif pointing == "right" and in_bounds((guard[0] ,guard[1] + 1),pointingDirection):
        if arr[guard[0], guard[1]+1] == "#":
            pointingDirection += 90
        else:
            guard = (guard[0], guard[1]+1)
    
    elif pointing == "down" and in_bounds((guard[0] + 1, guard[1]),pointingDirection):
        if arr[guard[0] + 1, guard[1]] == "#":
            pointingDirection += 90
        else:
            guard = (guard[0] + 1, guard[1])
        
    elif pointing == "left" and in_bounds((guard[0] ,guard[1] - 1),pointingDirection):
        if arr[guard[0], guard[1]-1] == "#":
            pointingDirection += 90
        else:
            guard = (guard[0], guard[1]-1)
        
    else:
        print("Out of bounds")
        break
        

    

print(tilesChecked+1) # Correct :) 4752
print(f"The total execution time is: {time.time()-start_time}")
    




# print(guard)
# updated_guard = (guard[0] + 1, guard[1] + 1)
# print(updated_guard)
# print(arr[guard]) 

