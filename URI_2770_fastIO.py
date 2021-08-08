import sys

while True:
    try:
        pcb_base_x, pcb_base_y, requests_qty = map(int, sys.stdin.readline().strip().split())
    except:
        break

    pcb_client = [tuple(map(int, sys.stdin.readline().strip().split())) for line in range(requests_qty)]
    is_possible = ['Sim' if (pcb[0] <= pcb_base_x and pcb[1] <= pcb_base_y) or\
                            (pcb[1] <= pcb_base_x and pcb[0] <= pcb_base_y) else\
                   'Nao' for pcb in pcb_client]
    sys.stdout.write('\n'.join(is_possible))


