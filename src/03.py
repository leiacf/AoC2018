# AoC 2018 Day 3

filename="../input/03.txt"

with open(filename, "r") as f:
    raw = f.readlines()
    f.close()

def parse(raw):

    data = []

    for line in raw:
        line = line.strip()

        line = line.replace("#", "")
        line = line.replace(" @", "")
        line = line.replace(",", " ")
        line = line.replace(":", "")
        line = line.replace("x", " ")

        data.append(line.split())

    return data

def fill(data):

    # id left top wide tall

    coords = {}

    for entry in data:

        xmin = int(entry[1])
        xmax = int(entry[3])
        ymin = int(entry[2])
        ymax = int(entry[4])

        for x in range (xmin, xmin+xmax):
            for y in range (ymin, ymin+ymax):

                coord = (x,y)

                if coord not in coords:
                    coords[coord] = 1
                else:
                    coords[coord] += 1

    return coords

def calculate(coords):

    total = 0
    
    for key, value in coords.items():

        if value > 1:
            total += 1

    return total


# Part 1

data = parse(raw)
coords = fill(data)

print("The number of square inches within two or more claims are", calculate(coords))