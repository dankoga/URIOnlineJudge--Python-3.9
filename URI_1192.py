if __name__ == '__main__':
    for _ in range(int(input())):
        instruction = input()
        if instruction[0] == instruction[2]:
            print(int(instruction[0]) * int(instruction[2]))
        elif instruction[1].isupper():
            print(int(instruction[2]) - int(instruction[0]))
        else:
            print(int(instruction[0]) + int(instruction[2]))
