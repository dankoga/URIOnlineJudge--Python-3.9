fruits_test_sz, fruits_database_sz = map(int, input().split())
fruits_test = [input().lower() for f in range(fruits_test_sz)]
fruits_database = [input().lower() for f in range(fruits_database_sz)]

for fruit_t in fruits_test:
    is_liked = False
    for fruit_db in fruits_database:
        if fruit_t in fruit_db or fruit_t in fruit_db[::-1]:
            is_liked = True
            break
    if is_liked:
        print('Sheldon come a fruta {}'.format(fruit_t))
    else:
        print('Sheldon detesta a fruta {}'.format(fruit_t))
