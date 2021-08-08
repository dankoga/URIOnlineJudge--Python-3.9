def largest(number_a, number_b):
    return (number_a + number_b + abs(number_a - number_b))//2

number_A, number_B, number_C = map(int, input().split())

print("{} eh o maior".format(largest(number_A, largest(number_B, number_C))))