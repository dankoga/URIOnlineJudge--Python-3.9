while True:
    try:
        library_size = int(input())
    except EOFError:
        break

    library = [input() for book in range(library_size)]
    print('\n'.join([book for book in sorted(library)]))
