import numpy as np

def calculate_fuel_cost(mass):
    neededFuel =  (mass//3) - 2
    if neededFuel < 0:
        return 0
    return neededFuel

def recursive_calculation(mass):
    neededfuel = calculate_fuel_cost(mass)
    if neededfuel <= 0:
        return 0
    return neededfuel + recursive_calculation(neededfuel) 



with open("dayOne.txt","r") as f:
    lines = f.readlines()

partOne = np.array([(int(line.strip())//3) - 2 for line in lines]).sum()

partTwo = np.array([recursive_calculation(int(line.strip())) for line in lines]).sum()


print(f"Part One results in: {partOne}")
print(f"Part Two results in: {partTwo}")