import time

start_time = time.time()

result = 0

with open("dayTwo.txt","r") as f:
    for line in f:
        sum = True
        data = tuple(map(int,line.strip().split()))
        if tuple(sorted(data)) == data or tuple(sorted(data)) == data[::-1]:
            n = data[0]
            for number in data[1:]:
                if number == n or abs(number-n) > 3:
                    sum = False
                    break
                n = number
            if sum:
                result += 1
        else:
            continue

            

print(result)
print("Total execution time was: " + str(time.time()-start_time))


# 224
# Correct :)