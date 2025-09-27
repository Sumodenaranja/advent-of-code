path = "dayOne.txt"

lists = []

with open(path,"r") as file:
    for line in file:
        lists.append(line.strip())

for item in lists:
    num = 0
    numb = 0
    while num <= len(lists)-1:
        while numb <=len(lists)-1:
            if int(item) + int(lists[int(num)]) + int(lists[int(numb)]) == 2020:
                print(int(item) * int(lists[num]) * int(lists[numb]))
            numb += 1 
        num += 1

