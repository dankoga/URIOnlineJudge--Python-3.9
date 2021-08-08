while True:
    try:
        tree_width = int(input())
    except EOFError:
        break
    half_width = tree_width // 2
    tree_body = [' ' * (half_width - w) + '*' * (2 * w + 1) for w in range(half_width + 1)]
    print('\n'.join(tree_body))
    print('\n'.join(tree_body[:2]))
    print()
