if __name__ == '__main__':
    number_freq = dict()
    data_size = int(input())
    for _ in range(data_size):
        n = int(input())
        if n in number_freq:
            number_freq[n] += 1
        else:
            number_freq[n] = 1
    for number, freq in [(x[0], x[1]) for x in sorted(number_freq.items())]:
        print('{} aparece {} vez(es)'.format(number, freq))
