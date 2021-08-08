even_qty = 0
positive_qty = 0
negative_qty = 0
for inputs in range(5):
    number = float(input())
    even_qty += int(number % 2 == 0)
    positive_qty += int(number > 0)
    negative_qty += int(number < 0)
print('{} valor(es) par(es)'.format(even_qty))
print('{} valor(es) impar(es)'.format(5 - even_qty))
print('{} valor(es) positivo(s)'.format(positive_qty))
print('{} valor(es) negativo(s)'.format(negative_qty))