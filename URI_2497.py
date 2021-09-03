if __name__ == '__main__':
    experiment_no = 1
    while True:
        steps = int(input())
        if steps < 0:
            break
        print('Experiment {}: {} full cycle(s)'.format(experiment_no, steps // 2))
        experiment_no += 1
