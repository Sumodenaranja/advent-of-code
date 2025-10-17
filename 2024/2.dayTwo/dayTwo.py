result = 0

with open("dayTwo.txt", "r") as f:
    for line in f:
        sum = True

        values = list(map(int,line.strip().split()))

        if sorted(values) == values or sorted(values) == values[::-1]:
            for v1, v2 in zip(values[:-1],values[1:]):

                if (abs(v1-v2) > 3) or (v1 == v2):
                    sum = False
                    break
            
            if sum:
                result += 1

print(result)
            
