if __name__ == '__main__':
    distances = []
    while True:
        try:
            input()
        except EOFError:
            break
        distances.append(float(input()))
    print('{:.1f}'.format(sum(distances) / len(distances)))
