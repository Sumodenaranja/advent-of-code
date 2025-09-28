import numpy as np

arr = np.zeros([1000,1000],dtype=int)

with open("daySix.txt","r") as f:
    for line in f:
        line = line.strip()
        instructions = line.split()

        if instructions[0] == "toggle":
            startPos = tuple(map(int, instructions[1].split(",")))
            endPos = tuple(map(int, instructions[-1].split(",")))
            arr[startPos[0]:endPos[0]+1,startPos[1]:endPos[1]+1] = 1 - arr[startPos[0]:endPos[0]+1,startPos[1]:endPos[1]+1]
        else:
            state = 1 if instructions[1] == "on" else 0
            startPos = tuple(map(int, instructions[2].split(",")))
            endPos = tuple(map(int, instructions[-1].split(",")))

            arr[startPos[0]:endPos[0]+1,startPos[1]:endPos[1]+1] = state

print(arr.sum())