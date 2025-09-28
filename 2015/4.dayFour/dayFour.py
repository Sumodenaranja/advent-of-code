import hashlib

with open("dayFour.txt", "r") as f:
    secret_key = f.read().rstrip()

number = 0

hex_result = ""

check_five_zeros = True

# Solution to Part Two
while not hex_result.startswith("000000"):

    # Solution to Part One
    if hex_result.startswith("00000") and check_five_zeros:
        print(number)
        check_five_zeros = False

    number += 1
    message = (secret_key + str(number)).encode()

    digest = hashlib.md5(message)

    hex_result = digest.hexdigest()

print(number)
    


