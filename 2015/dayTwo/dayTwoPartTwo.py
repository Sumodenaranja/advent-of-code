result = 0

with open("dayTwo.txt", "r") as f:
    for line in f:
        line = line.strip()
        l, w, h = map(int, line.split("x"))

        smallest_perimeter = 2*(min((l+w),(w+h),(h+l)))
        bow = (l*w*h)

        result += smallest_perimeter+ bow

print(result)