import time

start_time = time.time()

result = 0

with open("dayThree.txt","r") as f:
    for line in f:
        while line.find("mul(") != -1:
            found = line.find("mul(")
            
            line = line[found+4:]
            end = line.find(")")
            if line.find(","):
                numbers = line[:end].split(",")
                if len(numbers) == 2 and numbers[0].isnumeric() and numbers[1].isnumeric():
                    result += int(numbers[0])*int(numbers[1])
                        

            
                    


print(result)
print("Total execution time was: " + str(time.time()-start_time))

# 180233229 Correct :)