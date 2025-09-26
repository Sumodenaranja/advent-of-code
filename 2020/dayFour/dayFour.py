data = open("dayFour.txt","r").read().rstrip().split()

def part_one():
    total_score = 0
    
    for line in data:
        elfs = line.split(",")
        r1 = elfs[0].split("-")
        r2 = elfs[1].split("-")
        if r1[0]<=r2[0] and r1[1]>=r2[1]or r2[0]<=r1[0] and r2[1]>=r1[1]:
            print (r1, r2)
            total_score += 1
            print (total_score)
    print(total_score)

part_one()
        