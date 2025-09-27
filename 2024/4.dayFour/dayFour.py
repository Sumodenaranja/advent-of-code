import time

start_time = time.time()

result = 0
vertical = -1

executions = 0
#This is a 140x140 square


# We will divide this code in four different phases for each line

with open("dayFour.txt","r") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        #First we will check horizontaly
        for (one,two,three,four) in zip(line,line[1:],line[2:],line[3:]):
            if (one,two,three,four) == ("X","M","A","S") or (one,two,three,four) == ("S","A ","M","X"):
                result += 1
        
        vertical += 1

        executions += 1
        #Then we check verticaly
        
        groupOfFour = lines[vertical:vertical+4]
        for column in range(len(line)):
            chars = tuple(line[column] for line in groupOfFour)
            if chars == ("X", "M", "A", "S") or chars == ("S", "A", "M", "X"):
                result += 1
        
        #Diagonaly starting from top left
        for column in range(len(line)-3):
            chars = tuple(line[column+i] for i,line in enumerate(groupOfFour))
            if chars == ("X", "M", "A", "S") or chars == ("S", "A", "M", "X"):
                result += 1

        #Diagonaly starting from top right
        for column in range(3,len(line)):
            chars = tuple(line[column-i] for i,line in zip(range(4),groupOfFour))
            if chars == ("X", "M", "A", "S") or chars == ("S", "A", "M", "X"):
                result += 1

                        

            
             
# for (one,two,three,four) in zip(groupOfFour[0:],groupOfFour[1:],groupOfFour[2:],groupOfFour[3:]):


print(result)
print(executions)
print("Total execution time was: " + str(time.time()-start_time))

# 2536 Correct :)