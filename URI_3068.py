farm_x1, farm_y1, farm_x2, farm_y2 = map(int, input().split())
test_number = 1
while all([farm_x1, farm_x2, farm_y1, farm_y2 != 0]):
    meteor_qty = int(input())
    meteor_inside = 0
    for m in range(meteor_qty):
        meteor_x, meteor_y = map(int, input().split())
        meteor_inside += int((farm_x1 <= meteor_x <= farm_x2) and (farm_y2 <= meteor_y <= farm_y1))
    print('Teste {}\n{}'.format(test_number, meteor_inside))
    test_number += 1
    farm_x1, farm_y1, farm_x2, farm_y2 = map(int, input().split())
