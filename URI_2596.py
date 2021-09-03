from math import floor, sqrt

if __name__ == '__main__':
    cases_qty = int(input())
    for c in range(cases_qty):
        balls = float(input())
        print('{:.0f}'.format(balls - floor(sqrt(balls))))
