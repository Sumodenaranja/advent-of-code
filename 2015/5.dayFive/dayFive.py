disallowed_substrings = ["ab", "cd", "pq", "xy"]

nice_strings = 0

with open("dayFive.txt","r") as f:
    for string in f:
        string = string.strip()

        has_double = any(l1 == l2 for l1,l2 in zip(string[:-1], string[1:]))
        disallowed = any(bad in string for bad in disallowed_substrings)
        has_three_vowels = (sum(1 for v in string if v in "aeiou")) >= 3
        
        if has_three_vowels and has_double and not disallowed:
            nice_strings += 1

print(nice_strings)