from math import dist

if __name__ == '__main__':
    cases_qty = int(input())
    for c in range(cases_qty):
        balls_qty = int(input())
        cue_position = list(map(float, input().split()))
        balls_distance = [(dist(cue_position,list(map(float, input().split()))), i) for i in range(1, balls_qty + 1)]
        print(sorted(balls_distance)[0][1])
