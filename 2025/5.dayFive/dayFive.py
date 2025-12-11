itemsToCheck = []
freshRanges = []
freshItems = 0
totalFreshItems = 0
with open("dayFive.txt", "r") as file:
    for line in file:
        line = line.strip()

        if len(line.split("-")) == 2:
            splitedLine = line.split("-")
            freshRanges.append((int(splitedLine[0]), int(splitedLine[1])))
        else:
            itemsToCheck.append(int(line))

for item in itemsToCheck:
    for (k,v) in freshRanges:
        if k <= item <= v:
            freshItems += 1
            break

print(f'Result to part one: {freshItems}')
