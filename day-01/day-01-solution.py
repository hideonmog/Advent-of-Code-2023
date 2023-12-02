# Part 1

with open("input.txt") as f:
    calibrations = f.read().splitlines()

result = 0
for x in calibrations:
    digits = [ch for ch in x if ch.isdigit()]
    result += int(digits[0] + digits[-1])
print("Part 1:", result)

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

result = 0
for x in calibrations:
    s = ""
    for ch in x:
        s += ch
        for k, v in numbers.items():
            if s.endswith(k):
                s = s[:-1] + numbers[k] + s[-1:]
    digits = [ch for ch in s if ch.isdigit()]
    result += int(digits[0] + digits[-1])

print("Part 2:", result)
