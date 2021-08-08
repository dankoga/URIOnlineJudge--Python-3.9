def bf_to_py():
    instructions = [symbol for symbol in input() if symbol in '<>-+[].,#']
    source_list = ['pointer_mem = pointer_inp = 0']
    indentation = 0
    n = 0
    while n < len(instructions):
        symbol = instructions[n]
        if symbol == '[':
            source_list += [indentation * '    ' + 'while memory[pointer_mem] != 0:']
            n += 1
            indentation += 1
        elif symbol == ']':
            indentation -= 1
            n += 1
        elif symbol == '.':
            source_list += [indentation * '    ' + 'output_stream += [memory[pointer_mem]]']
            n += 1
        elif symbol == '#':
            source_list += [indentation * '    ' + 'output_stream += memory[:10]']
            n += 1
        elif symbol == ',':
            source_list += [indentation * '    ' + 'if pointer_inp < len(input_stream):']
            source_list += [(indentation + 1) * '    ' + 'memory[pointer_mem] = input_stream[pointer_inp]']
            source_list += [(indentation + 1) * '    ' + 'pointer_inp += 1']
            source_list += [indentation * '    ' + 'else:']
            source_list += [(indentation + 1) * '    ' + 'memory[pointer_mem] = 0']
            n += 1
        else:
            counter = 0
            while n < len(instructions) and instructions[n] == symbol:
                counter += 1
                n += 1
            if symbol == '>':
                source_list += [indentation * '    ' + 'pointer_mem = (pointer_mem + {}) % 30000'.format(counter)]
            elif symbol == '<':
                source_list += [indentation * '    ' + 'pointer_mem = (pointer_mem - {}) % 30000'.format(counter)]
            elif symbol == '+':
                source_list += [
                    indentation * '    ' + 'memory[pointer_mem] = (memory[pointer_mem] + {}) % 256'.format(counter)]
            elif symbol == '-':
                source_list += [
                    indentation * '    ' + 'memory[pointer_mem] = (memory[pointer_mem] - {}) % 256'.format(counter)]
    return '\n'.join(source_list)


instances_qty = int(input())
for i in range(1, instances_qty + 1):
    input()
    input_stream = [ord(n) for n in input()]
    output_stream = []
    memory = [0 for m in range(30000)]

    source_py = bf_to_py()
    exec(source_py)
    print('Instancia {}'.format(i))
    print(''.join([chr(c) for c in output_stream]))
    print()
