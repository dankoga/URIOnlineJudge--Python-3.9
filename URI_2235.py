credits_value = list(map(int, input().split()))
if credits_value[0] == credits_value[1] or \
   credits_value[0] == credits_value[2] or \
   credits_value[1] == credits_value[2] or \
   credits_value[0] == credits_value[1] + credits_value[2] or \
   credits_value[1] == credits_value[0] + credits_value[2] or \
   credits_value[2] == credits_value[0] + credits_value[1]:
    print('S')
else:
    print('N')
