filepath = "dayOne.txt"

result = 0

with open(filepath) as fp:
   for line in fp:
        line = fp.readline()
        line = line.strip()
        result += (int(line)//3)-2
   
print(result)