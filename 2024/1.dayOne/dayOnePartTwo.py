from collections import Counter
import time

start_time = time.time()

result = 0
 
with open("dayOne.txt","r") as f:
    pairs = [tuple(map(int, line.strip().split())) for line in f]
    

left,right = zip(*pairs)

countRight = Counter(right)

for number in left:
    if number in countRight.keys():
        result += number*countRight[number]

print(result)
print("Total execution time was: " + str(time.time()-start_time))

# 27647262
# Correct :)