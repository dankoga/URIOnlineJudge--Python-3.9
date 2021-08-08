MESSAGES = ['Bom Dia!!',
            'Boa Tarde!!',
            'Boa Noite!!',
            'De Madrugada!!',
            'Bom Dia!!']

while True:
    try:
        angular_position = float(input())
    except EOFError:
        break

    time_seconds = int(240.0 * angular_position)
    time_hours, time_seconds = divmod(time_seconds, 3600)
    time_minutes, time_seconds = divmod(time_seconds, 60)

    print(MESSAGES[time_hours // 6])
    print('{:02d}:{:02d}:{:02d}'.format((time_hours + 6) % 24, time_minutes, time_seconds))
