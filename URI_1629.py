def digital_sum(n):
    n, result = divmod(n, 10)
    while n > 0:
        n, digit = divmod(n, 10)
        result += digit
    return result


while True:
    tests_qty = int(input())
    if tests_qty == 0:
        break
    for t in range(tests_qty):
        number = input()
        counter_A = counter_B = 0
        for i in range(0, len(number), 2):
            counter_A += int(number[i])
        for i in range(1, len(number), 2):
            counter_B += int(number[i])
        print(digital_sum(counter_A) + digital_sum(counter_B))
