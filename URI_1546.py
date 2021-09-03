NAMES_TABLE = ['', 'Rolien', 'Naej', 'Elehcim', 'Odranoel']


if __name__ == '__main__':
    days = int(input())
    for _ in range(days):
        feedback_qty = int(input())
        for _ in range(feedback_qty):
            print(NAMES_TABLE[int(input())])
