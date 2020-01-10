def perform_operation(opcode, in1, in2):
    opcode = int(opcode)
    in1 = int(in1)
    in2 = int(in2)
    if opcode == 1:
        return in1 + in2
    elif opcode == 2:
        return in1 * in2
    else:
        return None

def run_file(filename, output):
    with open(filename, "r") as file:
        data = file.read().split(",")
    data = filter(None, data)
    data = list(map(int, data))
    if len(data) >= 4:
        i = 0
        while i < len(data) and data[i] != 99:
            data[data[i + 3]] = perform_operation(
                data[i], data[data[i + 1]], data[data[i + 2]]
            )
            i += 4
    with open(output, "w") as file:
        first_element = True
        for point in data:
            if first_element:
                file.write(str(point))
                first_element = False
            else:
                file.write("," + str(point))


if __name__ == "__main__":
    run_file("input.txt", "output.txt")
