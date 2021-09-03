import sys

DEZENAS = ['',
           'um',
           'dois',
           'tres',
           'quatro',
           'cinco',
           'seis',
           'sete',
           'oito',
           'nove',
           'dez',
           'onze',
           'doze',
           'treze',
           'quatorze',
           'quinze',
           'dezesseis',
           'dezessete',
           'dezoito',
           'dezenove',
           'vinte',
           'vinte e um',
           'vinte e dois',
           'vinte e tres',
           'vinte e quatro',
           'vinte e cinco',
           'vinte e seis',
           'vinte e sete',
           'vinte e oito',
           'vinte e nove',
           'trinta',
           'trinta e um',
           'trinta e dois',
           'trinta e tres',
           'trinta e quatro',
           'trinta e cinco',
           'trinta e seis',
           'trinta e sete',
           'trinta e oito',
           'trinta e nove',
           'quarenta',
           'quarenta e um',
           'quarenta e dois',
           'quarenta e tres',
           'quarenta e quatro',
           'quarenta e cinco',
           'quarenta e seis',
           'quarenta e sete',
           'quarenta e oito',
           'quarenta e nove',
           'cinquenta',
           'cinquenta e um',
           'cinquenta e dois',
           'cinquenta e tres',
           'cinquenta e quatro',
           'cinquenta e cinco',
           'cinquenta e seis',
           'cinquenta e sete',
           'cinquenta e oito',
           'cinquenta e nove',
           'sessenta',
           'sessenta e um',
           'sessenta e dois',
           'sessenta e tres',
           'sessenta e quatro',
           'sessenta e cinco',
           'sessenta e seis',
           'sessenta e sete',
           'sessenta e oito',
           'sessenta e nove',
           'setenta',
           'setenta e um',
           'setenta e dois',
           'setenta e tres',
           'setenta e quatro',
           'setenta e cinco',
           'setenta e seis',
           'setenta e sete',
           'setenta e oito',
           'setenta e nove',
           'oitenta',
           'oitenta e um',
           'oitenta e dois',
           'oitenta e tres',
           'oitenta e quatro',
           'oitenta e cinco',
           'oitenta e seis',
           'oitenta e sete',
           'oitenta e oito',
           'oitenta e nove',
           'noventa',
           'noventa e um',
           'noventa e dois',
           'noventa e tres',
           'noventa e quatro',
           'noventa e cinco',
           'noventa e seis',
           'noventa e sete',
           'noventa e oito',
           'noventa e nove',
           'cem']

CENTENAS = ['',
            'cento',
            'duzentos',
            'trezentos',
            'quatrocentos',
            'quinhentos',
            'seiscentos',
            'setecentos',
            'oitocentos',
            'novecentos']


def number_to_name(number_str):
    number_int = int(number_str)
    if number_int <= 100:
        return DEZENAS[number_int]

    name = [CENTENAS[int(number_str[0])], DEZENAS[int(number_str[1:])]]
    return ' e '.join([n for n in name if len(n) > 0])


for input_line in sys.stdin:
    number = '{:0>6}'.format(input_line.rstrip())
    if int(number) == 0:
        print('zero')
        continue
    if int(number[:3]) == 0:
        print(number_to_name(number[3:]))
        continue

    if int(number[:3]) == 1:
        milhares = 'mil'
    else:
        milhares = number_to_name(number[:3]) + ' mil'

    if int(number[3:]) == 0:
        centenas = ''
    elif int(number[3:]) < 100 or int(number[3:]) % 100 == 0:
        centenas = 'e ' + number_to_name(number[3:])
    else:
        centenas = number_to_name(number[3:])

    print(' '.join([n for n in [milhares, centenas] if len(n) > 0]))
