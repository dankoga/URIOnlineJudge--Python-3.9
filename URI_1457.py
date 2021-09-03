def k_factorial(n, k):
    result = 1
    for f in range(n, 0, -k):
        result *= f
    return result


if __name__ == '__main__':
    instances = int(input())
    for i in range(instances):
        number, *operator = input().split('!')
        print(k_factorial(int(number), len(operator)))
