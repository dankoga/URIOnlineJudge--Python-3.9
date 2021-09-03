if __name__ == '__main__':
    towers_qty = int(input())
    towers_per_height = dict()
    for height in map(int, input().split()):
        if height in towers_per_height:
            towers_per_height[height] += 1
        else:
            towers_per_height[height] = 1

    remaining_towers = towers_qty
    uses = [remaining_towers]
    for item in sorted(towers_per_height.items(), key=lambda x: x[0]):
        remaining_towers -= item[1]
        uses.append(item[0] + remaining_towers)

    print(min(uses))

