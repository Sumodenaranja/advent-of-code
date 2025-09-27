path = "dayOne.txt"

lists = []
temp = 0

with open(path, "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            lists.append(temp)
            temp = 0
        else:
            temp = temp + int(line)

print("The number 1 monkey with the most calories has: " + str(max(lists)) + " calories")

sum = max(lists)

for item in range(2,4):
    nah = 0
    monke = max(lists)
    position = [i for i, j in enumerate(lists) if j == monke]
    for pos in position:
        nah = nah + pos
    lists.pop(int(nah))
    sum = sum + max(lists)
    print("The number "+ str(item) + " monkey with the most calories has: " + str(max(lists)) + " calories")
   
print("The three monkeys with the most calories, have " + str(sum) + " calories")

