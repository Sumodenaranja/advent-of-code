data = open("dayTwo.txt","r").read().rstrip().split()


total = 0
for line in data:
    l, w, h = line.split("x")
    l,w,h = int(l), int(w), int(h)
    smallestArea = l*h
    total += ((2*l*w) + (2*w*h) + (2*h*l))+smallestArea 


#1690735 Too high
print(total)