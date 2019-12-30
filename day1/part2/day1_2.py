def calculateFuel(mass):
    return max((int(mass) // 3) - 2, 0)

def fuelRequired(mass):
    fuel = 0
    fuelCalc = calculateFuel(mass)
    while(fuelCalc > 0):
        fuel += fuelCalc
        fuelCalc = calculateFuel(fuelCalc)
    return fuel


def totalFuelFromFile(filename):
    sum = 0
    massArray = open(filename, "r").readlines()
    for mass in massArray:
        sum += fuelRequired(mass)
    return sum

if __name__ == '__main__':
    result = totalFuelFromFile("mass.txt")
    print(result)