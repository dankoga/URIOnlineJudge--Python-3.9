while True:
    lines_qty = int(input())
    if lines_qty == 0:
        break

    text = ''.join(input() for i in range(lines_qty))
    digrams_freq = {}
    for c in range(len(text) - 1):
        digram = text[c:c+2]
        if digram in digrams_freq:
            digrams_freq[digram] += 1
        else:
            digrams_freq[digram] = 1

    digrams_list = [[digram, freq] for digram, freq in sorted(digrams_freq.items(), key=lambda x: (-x[1], x[0]))]
    freq_total = sum([x[1] for x in digrams_list])
    for digram in digrams_list[:5]:
        print('{} {} {:.6f}'.format(digram[0], digram[1], digram[1] / freq_total))
    print()
