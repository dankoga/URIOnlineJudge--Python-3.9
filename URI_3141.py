name = input()
today_date = list(map(int, input().split('/')))
birth_date = list(map(int, input().split('/')))

birth_year_date = birth_date[1] * 100 + birth_date[0]
today_year_date = today_date[1] * 100 + today_date[0]

if today_year_date == birth_year_date:
    print('Feliz aniversario!')
age = today_date[2] - birth_date[2] - 1 + int(today_year_date >= birth_year_date)
print('Voce tem {} anos {}.'.format(age, name))
