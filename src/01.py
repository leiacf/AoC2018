# AoC 2018 Day 1

file="../input/01.txt"

with open(file, "r") as f:
    data = f.readlines()
    f.close()


def parse(data):

    total = 0

    for line in data:

        line = line.strip()

        operand = line[:1]
        number = int(line[1:])

        if operand == "+":
            total += number
        elif operand == "-":
            total -= number

    return total

# Part 1

print("The total is: ", parse(data))

