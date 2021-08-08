while True:
    try:
        input_expression = input()
    except EOFError:
        break
    operands = input_expression.replace('+', '=').split('=')
    if operands[2].isalpha():
        print(int(operands[0]) + int(operands[1]))
    elif operands[1].isalpha():
        print(int(operands[2]) - int(operands[0]))
    else:
        print(int(operands[2]) - int(operands[1]))
