with open("dayTwo.txt","r") as f:
    original_numbers = list(map(int, f.readline().strip().split(",")))



for noun in range(100):
    for verb in range(100):

        numbers = original_numbers.copy()
        i = 0

        numbers[1] = noun
        numbers[2] = verb

        while i < len(numbers):
            if numbers[i] == 1:
                numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
            elif numbers[i] == 2:
                numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]
            elif numbers[i] == 99:
                break    
            else:
                raise Exception("The instruction is not 1,2 or 99")
            
            i += 4 # 4 Because the blocks are made of 4 instructions


        if noun == 12 and verb == 2:
            print(f"Solution part one: {numbers[0]}")
        if numbers[0] == 19690720:
            print(f"Solution part two: {100 * numbers[1] + numbers[2]}")
            break

            
        


