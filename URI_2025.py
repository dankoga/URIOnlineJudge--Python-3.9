import re


oulupukk = re.compile(r".oulupukk.")
lines_qty = int(input())
for line in range(lines_qty):
    print(re.sub(oulupukk, 'Joulupukki', input()) )
