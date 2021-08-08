while True:
    try:
        sprints_qty = int(input())
    except EOFError:
        break
    sprints_times = [float(input()) for s in range(sprints_qty)]
    print(min(sprints_times))
