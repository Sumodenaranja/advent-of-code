import time

start_time = time.time()
left = []
right = []
result = 0

with open("dayOne.txt","r") as f:
    for line in f:
        line = line.strip()
        spRight,spLeft = line.split() #sp = split
        left.append(int(spRight))
        right.append(int(spLeft))

left.sort()
right.sort()

i = 0
while i<len(left):
    result += abs(left[i]-right[i])
    i+=1

print(result)
print("Total execution time was: " + str(time.time()-start_time))

# 2344935
# Correct :)