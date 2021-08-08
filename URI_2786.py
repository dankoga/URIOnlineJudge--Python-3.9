length = int(input())
width = int(input())
print('{}\n{}'.format(width * length + (width - 1) * (length - 1),
                      2 * (width + length - 2)))
