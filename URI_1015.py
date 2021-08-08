from math import sqrt

point_A = list(map(float, input().split()))
point_B = list(map(float, input().split()))

print("{:.4f}".format(sqrt((point_A[0] - point_B[0]) ** 2 + (point_A[1] - point_B[1]) ** 2)))
