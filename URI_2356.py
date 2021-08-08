while True:
    try:
        bacterial_dna = input()
    except EOFError:
        break
    if input() in bacterial_dna:
        print('Resistente')
    else:
        print('Nao resistente')
