def inverte(x, y, v):
    v[(x - 1):y] = (v[(x - 1):y])[::-1]
    return v


def soma(x, y, v):
    print(sum(v[(x - 1):y]))


if __name__ == '__main__':
    memory_size, instructions_qty = map(int, input().split())
    memory = list(range(1, memory_size + 1))
    for _ in range(instructions_qty):
        instruction, x, y = input().split()
        x = int(x)
        y = int(y)
        if instruction == 'I':
            memory = inverte(x, y, memory)
        else:
            soma(x, y, memory)
