itemsToCheck = []
freshRanges = []
freshItems = 0
totalFreshItems = 0
with open("dayFive.txt", "r") as file:
    for line in file:
        line = line.strip()
        added = False

        if len(line.split("-")) == 2:
            splitedLine = list(map(int,line.split("-")))
            for i, (k,v) in enumerate(freshRanges):
                if splitedLine[0] <= k and splitedLine[0] >= k:
                    freshRanges[i] = (splitedLine[0],freshRanges[i][1])
                    added = True
                if splitedLine[1] >= v and splitedLine[1] >= v:
                    freshRanges[i] = (freshRanges[i][0],splitedLine[1])
                    added = True
            if not added:
                freshRanges.append((splitedLine[0], splitedLine[1]))
        else:
            itemsToCheck.append(int(line))

for item in itemsToCheck:
    for (k,v) in freshRanges:
        if k <= item <= v:
            freshItems += 1
            break

for ran in freshRanges:
    totalFreshItems += abs(ran[0] - ran[1])


print(f'Result to part one: {freshItems}')
print(f'Result to part two: {totalFreshItems}')

# Too high 30692949720800917