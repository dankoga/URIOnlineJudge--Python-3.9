while True:
    number_broken, number_correct = input().split()
    if number_broken == number_correct == '0':
        break
    number_writen = number_correct.replace(number_broken,'')
    if len(number_writen) > 0:
        print(int(number_writen))
    else:
        print(0)
