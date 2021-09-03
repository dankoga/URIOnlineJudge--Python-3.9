if __name__ == '__main__':
    a ,b = map(int, input().split())
    print(((a + b) * (b - a + 1)) // 2)
