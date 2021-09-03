if __name__ == '__main__':
    cases_qty = int(input())
    for c in range(cases_qty):
        road_length, radar_coverage = map(int, input().split())
        print((road_length + radar_coverage - 1) // radar_coverage)
