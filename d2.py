from tqdm import tqdm


def intcode(tape):
    i = 0
    while tape[i] != 99:
        opcode = tape[i]
        a, b, c = tape[i+1:i+4]
        if opcode == 1:
            tape[c] = tape[a] + tape[b]
        elif opcode == 2:
            tape[c] = tape[a] * tape[b]
        else:
            raise Exception("Reached undefined opcode")
        i += 4
    return tape[0]


if __name__ == "__main__":
    program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]
    for i in tqdm(range(100)):
        for j in range(100):
            copy = program.copy()
            copy[1] = i
            copy[2] = j
            try:
                if intcode(copy) == 19690720:
                    print(100 * i + j)
            except:
                continue

