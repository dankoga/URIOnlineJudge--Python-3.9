import  sys

for input_line in sys.stdin:
    soldiers_a, soldiers_b = map(int, input_line.split())
    print(abs(soldiers_b - soldiers_a))
