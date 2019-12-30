def fuelRequired(mass):
    return max((int(mass) // 3) - 2, 0)


def totalFuelFromFile(filename):
    sum = 0
    massArray = open(filename, "r").readlines()
    for mass in massArray:
        sum += fuelRequired(mass)
    return sum

if __name__ == '__main__':
    result = totalFuelFromFile("mass.txt")
    print(result)