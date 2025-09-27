
with open("dayOne.txt", "r") as f:
    text = f.read().rstrip()

floor = 0

for num, letter in enumerate(text):
    if floor == -1:
        print(num)
        break
    if letter == "(":
        floor +=1
    elif letter == ")":
        floor -=1
