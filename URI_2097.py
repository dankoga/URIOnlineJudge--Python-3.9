import sys

NAMES = {'zero':   0,
         'um':     1,
         'dois':   2,
         'tres':   3,
         'quatro': 4,
         'cinco':  5,
         'seis':   6,
         'sete':   7,
         'oito':   8,
         'nove':   9,
         'dez':       10,
         'onze':      11,
         'doze':      12,
         'treze':     13,
         'quatorze':  14,
         'quinze':    15,
         'dezesseis': 16,
         'dezessete': 17,
         'dezoito':   18,
         'dezenove':  19,
         'vinte':    20,
         'trinta':   30,
         'quarenta': 40,
         'cinquenta': 50,
         'sessenta': 60,
         'setenta':  70,
         'oitenta':  80,
         'noventa':  90,
         'cem':          100,
         'cento':        100,
         'duzentos':     200,
         'trezentos':    300,
         'quatrocentos': 400,
         'quinhentos':   500,
         'seiscentos':   600,
         'setecentos':   700,
         'oitocentos':   800,
         'novecentos':   900}

for line in sys.stdin:
    number_name = line.rstrip().split()
    if number_name == ['zero']:
        print(0)
        continue
    number_orders_list = ['000' for order in range(5)]
    number_order = 0
    for name in number_name:
        if name == 'trilhao' or name == 'trilhoes':
            number_orders_list[4] = '{:0>3d}'.format(number_order)
            number_order = 0
            continue
        if name == 'bilhao' or name == 'bilhoes':
            number_orders_list[3] = '{:0>3d}'.format(number_order)
            number_order = 0
            continue
        if name == 'milhao' or name == 'milhoes':
            number_orders_list[2] = '{:0>3d}'.format(number_order)
            number_order = 0
            continue
        if name == 'mil':
            if number_order > 0:
                number_orders_list[1] = '{:0>3d}'.format(number_order)
            else:
                number_orders_list[1] = '001'
            number_order = 0
            continue
        if name != 'e':
            number_order += NAMES[name]
    number_orders_list[0] = '{:0>3d}'.format(number_order)
    print(''.join([n for n in number_orders_list[::-1]]).lstrip('0'))
