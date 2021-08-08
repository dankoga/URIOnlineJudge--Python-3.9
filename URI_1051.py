income = float(input())
if income <= 2000.00:
    print("Isento")
elif income <= 3000.00:
    income -= 2000.00
    print('R$ {:.2f}'.format(0.08 * income))
elif income <= 4500.00:
    income -= 3000.00
    bracket_tax = 0.08 * 1000.00
    print('R$ {:.2f}'.format(0.18 * income + bracket_tax))
else:
    income -= 4500.00
    bracket_tax = 0.08 * 1000.00 + 0.18 * 1500.00
    print('R$ {:.2f}'.format(0.28 * income + bracket_tax))
