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


def parse_and_check(data):

    total = 0
    seen = []

    while True:

        for line in data:

            line = line.strip()

            operand = line[:1]
            number = int(line[1:])

            if operand == "+":
                total += number
            elif operand == "-":
                total -= number

            if total not in seen:
                seen.append(total)
            else:
                return total

# Part 1

print("The total is: ", parse(data))

# Part 2

print("The total is: ", parse_and_check(data))