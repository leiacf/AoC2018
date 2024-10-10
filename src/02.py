# AoC 2018 Day 2

file = "../input/02.txt"

with open(file, "r") as f:
    raw = f.readlines()
    f.close()

def parse(raw):
    data = []
    
    for line in raw:
        line = line.strip()
        data.append(line)

    return data

data = parse(raw)

def has_two(line):

    for letter in line:
        if (line.count(letter) == 2):
            return True

    return False

def has_three(line):

    for letter in line:
        if (line.count(letter) == 3):
            return True

    return False

def compare(data):

    entries = []

    for line in data:
        for entry in entries:
            
            if len(line) == len(entry):

                differs = 0
                index = -1

                for x in range(0, len(line)):

                    if line[x] != entry[x]:
                        differs += 1
                        index = x

                if (differs == 1):
                    return "" + line[:index] + line[index+1:]

        entries.append(line) 

# Part 1

two = 0
three = 0

for line in data:
    if has_two(line):
        two += 1    
    if has_three(line):
        three += 1

print("The checksum is", two*three)

# Part 2

result = compare(data)
print("The answer is: " + result)