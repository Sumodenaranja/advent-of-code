filepath = 'C:\\Users\\Sumito\\Desktop\\Python\\AdventOfCode2021\\DayThree\\AdventDayThreeA.txt'

def split(word): 
    return [char for char in word]
one = 0
count = 0
zero = 0

with open(filepath) as fp:
   line = fp.readline()
   while line:
       data = ("{}".format(line.strip()))
       split_line = split(str(data))
       while count + 1 < 7:
            if split_line[count] == 1:
                one += 1
                print("One more one")
            elif split_line[count] == 0:
                print("One more zero")
                zero += 1
       
       line = fp.readline()

print("There are", one, "ones and", zero, "zeros")