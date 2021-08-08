from math import sqrt

while True:
    try:
        test_parameters = input()
    except EOFError:
        break

    data_points = list(map(float, input().split()))
    average = sum(data_points)/len(data_points)
    residues = [data - average for data in data_points]
    accuracy = sqrt(sum([data * data for data in residues])/(len(residues) - 1))
    print('{:.5f}'.format(accuracy))
