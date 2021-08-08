integer_part, decimal_part = input().split('.')
print('{}.{}'.format(decimal_part.lstrip('0'), integer_part))
