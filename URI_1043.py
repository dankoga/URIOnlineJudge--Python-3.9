sides_input = list(map(float, input().split()))
sides_sorted = sides_input.copy()
sides_sorted.sort()

if sides_sorted[0] + sides_sorted[1] > sides_sorted[2]:
    print("Perimetro = {:.1f}".format(sum(sides_input)))
else:
    print("Area = {:.1f}".format((sides_input[0] + sides_input[1])/2.0 * sides_input[2]))
