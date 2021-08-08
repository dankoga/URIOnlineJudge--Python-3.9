jewelry = set()
while True:
    try:
        jewel = input()
    except EOFError:
        break
    jewelry.add(jewel)
print(len(jewelry))
