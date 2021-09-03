import sys

distance = 0.0
speed = 0.0
time_last_checkpoint = 0
for input_line in sys.stdin:
    time, *speed_new = input_line.split()
    time_h, time_m, time_s = map(int, time.split(':'))
    time_new_checkpoint = time_s + 60 * time_m + 3600 * time_h
    distance += speed * (time_new_checkpoint - time_last_checkpoint) / 3600.0
    time_last_checkpoint = time_new_checkpoint
    if len(speed_new) > 0:
        speed = float(speed_new[0])
    else:
        print(time + ' {:.2f} km'.format(distance))
