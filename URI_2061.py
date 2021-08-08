tabs_qty, actions_qty = map(int, input().split())
for action in range(actions_qty):
    action_string = input()
    if action_string == 'fechou':
        tabs_qty += 1
    else:
        tabs_qty -= 1
print(tabs_qty)
