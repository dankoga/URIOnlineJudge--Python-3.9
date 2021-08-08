while True:
    try:
        trainings_qty = int(input())
    except EOFError:
        break

    record_time, record_distance = map(int, input().split())
    print('1')
    for training in range(2,trainings_qty + 1):
        training_time, training_distance = map(int, input().split())
        if training_distance * record_time > training_time * record_distance:
            print(training)
            record_time = training_time
            record_distance = training_distance
