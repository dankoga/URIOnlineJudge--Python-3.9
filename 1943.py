if __name__ == '__main__':
    position = int(input())
    for last in [1, 3, 5, 10, 25, 50, 100]:
        if position <= last:
            print('Top {}'.format(last))
            break
