if __name__ == '__main__':
    participants_qty, budget, hotels_qty, weeks_qty = map(int, input().split())
    all_costs =[]
    for h in range(hotels_qty):
        cost = participants_qty * int(input())
        if any([beds >= participants_qty for beds in map(int, input().split())]):
            all_costs.append(cost)
    if len(all_costs) == 0 or min(all_costs) > budget:
        print('stay home')
    else:
        print(min(all_costs))
