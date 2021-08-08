from math import gcd


def vector_add(vector, begin, end, value):
    for index in range(begin, end):
        vector[index] += value


def vector_gcd(vector, begin, end):
    print(gcd(*(vector[begin:end])))


while True:
    try:
        vector_length, queries_qty = map(int, input().split())
    except EOFError:
        break
    number_vector = list(map(int, input().split()))
    for query in range(queries_qty):
        query_line = input()
        if len(query_line) == 0:
            print(query + 1)
            continue
        instruction, *operands = map(int, query_line.split())
        if instruction == 1:
            vector_add(number_vector, operands[0], operands[1], operands[2])
        else:
            vector_gcd(number_vector, operands[0], operands[1])
