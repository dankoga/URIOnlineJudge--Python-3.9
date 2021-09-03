while True:
    try:
        puppies_qty = int(input())
    except EOFError:
        break
    chosen_puppies = 0
    for p in range(puppies_qty):
        species = input()
        breed = input()
        name = input().split()
        blank = input()
        chosen_puppies += int(species == 'cachorro' and len(name) >= 2 and any([breed[0] == n[0] for n in name]))
    print(chosen_puppies)
