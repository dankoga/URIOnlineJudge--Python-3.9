while True:
    try:
        steps_qty = int(input())
    except EOFError:
        break
    entry_lines = list(map(int, input().split()))
    assembly_A = list(map(int, input().split()))
    assembly_B = list(map(int, input().split()))
    if steps_qty > 1:
        switch_AB = list(map(int, input().split()))
        switch_BA = list(map(int, input().split()))
    exit_lines = list(map(int, input().split()))

    assembly_A[0] += entry_lines[0]
    assembly_A[-1] += exit_lines[0]
    assembly_B[0] += entry_lines[1]
    assembly_B[-1] += exit_lines[1]

    for step in range(-1, -steps_qty, -1):
        assembly_A[step - 1] += min(assembly_A[step], assembly_B[step] + switch_AB[step])
        assembly_B[step - 1] += min(assembly_B[step], assembly_A[step] + switch_BA[step])
    print(min(assembly_A[0], assembly_B[0]))
