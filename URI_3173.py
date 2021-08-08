import datetime

years = float(input())

days_T = 365.25 * years
days_J = int(11.9 * days_T)
days_S = int(29.6 * days_T)
date_J = datetime.date(2020, 12, 21) + datetime.timedelta(days=days_J)
date_S = datetime.date(2020, 12, 21) + datetime.timedelta(days=days_S)

print('Dias terrestres para Jupiter = {}'.format(days_J))
print('Data terrestre para Jupiter: {}'.format(date_J))
print('Dias terrestres para Saturno = {}'.format(days_S))
print('Data terrestre para Saturno: {}'.format(date_S))
