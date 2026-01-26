import numpy as np
import time

start_time = time.time()

arr = np.empty((140, 140),dtype=object)
index = 0

with open("dayFour.txt","r") as file:
    for line in file:
        line = line.strip()
        for i, character in enumerate(line):
            arr[index,i] = character
        index += 1


result = 0
currentSwipe = 0
swipeNumber = 1
exit = False

positionsToRemove = []

while not exit:
    x = 0
    y = 0
    currentSwipe = 0
    positionsToRemove = []

    while x <= 139 and y <= 139:
        # Positions to check
        posiblePositions = [(x-1,y+1),(x-1,y), (x-1,y-1), (x,y+1), (x,y-1), (x+1,y+1),(x+1,y), (x+1,y-1)]
        paperRolls = 0
        
        if arr[x,y] == "@":
            posiblePositions = [
                (i, j)
                for (i, j) in posiblePositions
                if 0 <= i <= 139 and 0 <= j <= 139
            ]

            for position in posiblePositions:
                if arr[position[0],position[1]] == "@":
                    paperRolls += 1

            if paperRolls < 4:
                currentSwipe += 1
                positionsToRemove.append((x,y))

        x += 1
        if x == 140 :
            x = 0
            y += 1

    result += currentSwipe

    if currentSwipe == 0:
        exit = True

    if swipeNumber == 1:
        print("The result for the first part is: " + str(result))
    
    swipeNumber += 1

    for position in positionsToRemove:
        arr[position[0],position[1]] = "."

    

print("The result for the second part is: " + str(result))
print("It took " + str(swipeNumber) + " swipes to find the second part")
print("The program took " + str(time.time()-start_time) + " seconds to run.")