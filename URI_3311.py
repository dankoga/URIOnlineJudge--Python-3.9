clients_qty = int(input())
clients_names =[[input(), c] for c in range(clients_qty)]
print('\n'.join([client[0] for client in sorted(clients_names, key= lambda x: (x[0][0], x[1]))]))
