with open("dayTwo.txt","r") as f:
    numbers = list(map(int, f.readline().strip().split(",")))

numbers[1] = 12
numbers[2] = 2

i = 0

while i < len(numbers):
    if numbers[i] == 1:
        numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
    elif numbers[i] == 2:
        numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]
    elif numbers[i] == 99:
        print("Halt!")
        break
    else:
        raise Exception("The instruction is not 1,2 or 99")

    i += 4 # 4 Because the blocks are made of 4 instructions

print(numbers[0])
