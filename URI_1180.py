numbers_size = int(input())
numbers = list(map(int, input().split()))
numbers_indexed = [(numbers[index], index) for index in range(numbers_size)]
numbers_indexed.sort()
print('Menor valor: {}'.format(numbers_indexed[0][0]))
print('Posicao: {}'.format(numbers_indexed[0][1]))
