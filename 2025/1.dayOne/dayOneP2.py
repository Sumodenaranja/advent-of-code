
pointingAt = 50
total = 0
# Brute Force Solution
# TODO: Do something good
with open("dayOne.txt","r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]

        turn = int(line[1:])

        for i in range(turn):
            if direction == "L":
                pointingAt -=1
            elif direction == "R":
                pointingAt +=1
            
            pointingAt = (pointingAt)%100

            if pointingAt == 0:
                total +=1
        
print("The password is: " + str(total))
        