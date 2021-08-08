PI = 3.14159
parameter_A, parameter_B, parameter_C, = map(float, input().split())

print("TRIANGULO: {:.3f}".format(parameter_A * parameter_C / 2))
print("CIRCULO: {:.3f}".format(PI * parameter_C ** 2))
print("TRAPEZIO: {:.3f}".format((parameter_A + parameter_B) / 2 * parameter_C))
print("QUADRADO: {:.3f}".format(parameter_B ** 2))
print("RETANGULO: {:.3f}".format(parameter_A * parameter_B))
