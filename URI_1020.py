from sys import stdin

#days = int(stdin.readline())
days = int(input())
years, remainder = divmod(days, 365)
months, days = divmod(remainder, 30)
print("{} ano(s)".format(years))
print("{} mes(es)".format(months))
print("{} dia(s)".format(days))