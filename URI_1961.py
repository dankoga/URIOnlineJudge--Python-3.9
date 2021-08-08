jump_height, pipes_qty = map(int, input(). split())
pipes_height = list(map(int, input().split()))
pipes_diff = [abs(pipes_height[i] - pipes_height[i + 1]) for i in range(pipes_qty - 1)]
if max(pipes_diff) > jump_height:
    print('GAME OVER')
else:
    print('YOU WIN')
