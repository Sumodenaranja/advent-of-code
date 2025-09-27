import numpy as np

with open("dayOne.txt", "r") as f:
    text = f.read().rstrip()

myArray = np.array(list(text))

result = (myArray == "(").sum() - (myArray == ")").sum()

print(result)
