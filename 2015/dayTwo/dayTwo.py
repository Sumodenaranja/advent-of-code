result = 0

with open("dayTwo.txt", "r") as f:
    for line in f:
        line = line.strip()
        l, w, h = map(int, line.split("x"))

        result += (2*l*w + 2*w*h + 2*h*l) + (min((l*w),(w*h),(h*l)))

print(result)