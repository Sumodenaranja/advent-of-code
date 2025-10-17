left = []
right = []
result = 0

with open("dayOne.txt","r") as f:
    for line in f:
        line = line.strip()
        spRight,spLeft = line.split()
        left.append(int(spRight))
        right.append(int(spLeft))

left.sort()
right.sort()

i = 0
while i < len(left):
    result += abs(left[i]-right[i])
    i+=1

print(result)

