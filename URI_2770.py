while True:
    try:
        pcb_base_x, pcb_base_y, requests_qty = map(int, input().split())
    except EOFError:
        break
    pcb_client = [tuple(map(int, input().split())) for request in range(requests_qty)]
    is_possible = ['Sim' if (pcb[0] <= pcb_base_x and pcb[1] <= pcb_base_y) or\
                            (pcb[1] <= pcb_base_x and pcb[0] <= pcb_base_y) else\
                   'Nao' for pcb in pcb_client]
    print('\n'.join(is_possible))
