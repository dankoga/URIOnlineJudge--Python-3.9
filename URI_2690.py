TABLE_LETTERS = 'GQakuISblvEOYcmwFPZdnxJTeoyDNXfpzAKUgqCMWhrBLVisHRjt'
TABLE_NUMBERS = '0000011111222222333333444445555556666677777888889999'

tests_qty = int(input())
for t in range(tests_qty):
    password = input().replace(' ', '')[:12]
    print(password.translate(password.maketrans(TABLE_LETTERS, TABLE_NUMBERS)))
