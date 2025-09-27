result = 0

with open("dayTwo.txt", "r") as f:
    for line in f:
        l, w, h = map(int, line.strip().split("x"))

        result += (2*l*w + 2*w*h + 2*h*l) + (min((l*w),(w*h),(h*l)))

print(result)