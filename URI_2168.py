from operator import add


def print_security(array):
    for row in array:
        print(''.join('S' if x >= 2 else 'U' for x in row))

blocks_qty = int(input())
cameras_per_block = [[0 for col in range(blocks_qty)] for rows in range(blocks_qty)]

corner_cameras = list(map(int, input().split()))
cameras_view = list(map(add, corner_cameras[:-1], corner_cameras[1:]))
cameras_per_block[0] = list(map(add, cameras_per_block[0], cameras_view))
for row in range(1, blocks_qty):
    corner_cameras = list(map(int, input().split()))
    cameras_view = list(map(add, corner_cameras[:-1], corner_cameras[1:]))
    cameras_per_block[row] = list(map(add, cameras_per_block[row], cameras_view))
    cameras_per_block[row - 1] = list(map(add, cameras_per_block[row - 1], cameras_view))
corner_cameras = list(map(int, input().split()))
cameras_view = list(map(add, corner_cameras[:-1], corner_cameras[1:]))
cameras_per_block[-1] = list(map(add, cameras_per_block[-1], cameras_view))

print_security(cameras_per_block)
