TABLE_DIRECTION = ['N', 'L', 'S', 'O']


if __name__ == '__main__':
    while True:
        commands_qty = input()
        if commands_qty == '0':
            break
        direction = 0
        for command in input():
            direction += 137 - 2 * ord(command)
        print(TABLE_DIRECTION[direction % 4])