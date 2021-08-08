DDD_LIST = ['DDD nao cadastrado'] * 100
DDD_LIST[61] = 'Brasilia'
DDD_LIST[71] = 'Salvador'
DDD_LIST[11] = 'Sao Paulo'
DDD_LIST[21] = 'Rio de Janeiro'
DDD_LIST[32] = 'Juiz de Fora'
DDD_LIST[19] = 'Campinas'
DDD_LIST[27] = 'Vitoria'
DDD_LIST[31] = 'Belo Horizonte'

dialed_preffix = int(input())
print(DDD_LIST[dialed_preffix])
