import time

start_time = time.time()

result = 0

with open("AdventOfCode/2024/dayThree/dayThree.txt","r") as f:
    count = True
    for line in f:
        while line.find("mul(") != -1:
            found = line.find("mul(")
            do = line[:found].rfind("do()")
            dont = line[:found].rfind("don't()")
            print(line[:found])

            if do != -1 and dont !=-1:
                print("Do",do)
                print("Don't",dont)
                print(count)
                    
            if do != -1 and (dont == -1 or do > dont):
                count = True
            elif dont != -1 and (do == -1 or dont > do):
                count = False

            line = line[found+4:]
            end = line.find(")")
            if line.find(",") != -1:
                numbers = line[:end].split(",")
                if len(numbers) == 2 and numbers[0].isnumeric() and numbers[1].isnumeric():
                    if count == True:
                        result += int(numbers[0])*int(numbers[1])
                        

            
                    


print(result)
print("Total execution time was: " + str(time.time()-start_time))

# 95411583 Correct :)
