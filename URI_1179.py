def print_list(input_list, list_name):
    for index in range(len(input_list)):
        print(list_name + '[{}] = {}'.format(index, input_list[index]))

par = []
impar =[]
for input_line in range(15):
    number = int(input())
    if number % 2 == 0:
        par.append(number)
        if len(par) == 5:
            print_list(par, 'par')
            par.clear()
    else:
        impar.append(number)
        if len(impar) == 5:
            print_list(impar, 'impar')
            impar.clear()

print_list(impar, 'impar')
print_list(par, 'par')
