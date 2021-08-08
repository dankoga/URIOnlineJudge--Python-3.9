while True:
    try:
        trace = input()
    except EOFError:
        break
    processors_qty = int(input())
    cycles = 0
    read_counter = 0
    for instruction in trace:
        if instruction == 'R':
            read_counter += 1
        else:
            cycles += 1 + (read_counter + processors_qty - 1) // processors_qty
            read_counter = 0
    cycles += (read_counter + processors_qty - 1) // processors_qty
    print(cycles)
