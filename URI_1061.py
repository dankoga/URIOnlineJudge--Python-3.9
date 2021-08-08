begin_D = int(input().split()[1])
begin_H, begin_M , begin_S = map(int, input().split(':'))
end_D = int(input().split()[1])
end_H, end_M , end_S = map(int, input().split(':'))

delta_S = (end_S - begin_S) + 60 * (end_M - begin_M) + 3600 * (end_H - begin_H) + 86400 * (end_D - begin_D)
delta_D, delta_S = divmod(delta_S, 86400)
delta_H, delta_S = divmod(delta_S, 3600)
delta_M, delta_S = divmod(delta_S, 60)

print('{} dia(s)'.format(delta_D))
print('{} hora(s)'.format(delta_H))
print('{} minuto(s)'.format(delta_M))
print('{} segundo(s)'.format(delta_S))