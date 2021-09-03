if __name__ == '__main__':
    number_str = input()
    digital_sum = sum([int(d) for d in number_str])
    print((digital_sum - 48 * len(number_str)) % 3 )
