if __name__ == '__main__':
    days_per_year, people_qty = map(int, input().split())
    if people_qty <= days_per_year:
        prob = 1.0
        for p in range(people_qty):
            prob *= (days_per_year - p) / days_per_year
    else:
        prob = 0.0
    print('{:.2f}'.format((1.0 - prob) * 100.0))
