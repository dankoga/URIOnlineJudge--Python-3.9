if __name__ == '__main__':
    while True:
        if input().split() == ['0', '0']:
            break
        tickets = input().split()
        unique_tickets = dict()
        for t in tickets:
            if t in unique_tickets:
                unique_tickets[t] = 1
            else:
                unique_tickets[t] = 0
        print(sum([v for v in unique_tickets.values()]))
