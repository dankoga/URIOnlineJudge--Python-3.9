import re

number = input()
if re.match(r".*13.*", number):
    print('{} es de Mala Suerte'.format(number))
else:
    print('{} NO es de Mala Suerte'.format(number))
