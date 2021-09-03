if __name__ == '__main__':
    connector_A = list(map(int, input().split()))
    connector_B = list(map(int, input().split()))
    if all([a + b == 1 for a, b in zip(connector_A, connector_B)]):
        print('Y')
    else:
        print('N')
