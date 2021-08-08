numbers = list(map(int, input().split()))
if ((numbers[1] > numbers[2]) & (numbers[3] > numbers[0]) &
    (numbers[2] + numbers[3] > numbers[0] + numbers[1]) &
    (numbers[2] >= 0) & (numbers[3] >= 0) & (numbers[0] % 2 == 0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
