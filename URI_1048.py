wages = float(input())
if wages > 2000.00:
    increase_rate = 0.04
elif wages > 1200:
    increase_rate = 0.07
elif wages > 800:
    increase_rate = 0.10
elif wages > 400:
    increase_rate = 0.12
else:
    increase_rate = 0.15

wage_increase = wages * increase_rate
print("Novo salario: {:.2f}".format(wages + wage_increase))
print("Reajuste ganho: {:.2f}".format(wage_increase))
print("Em percentual: {:.0f} %".format(100*increase_rate))