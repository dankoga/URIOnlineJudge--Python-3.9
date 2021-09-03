import sys

if __name__ == '__main__':
    for p, input_line in enumerate(sys.stdin, start=1):
        value_investment, value_return = map(float, input_line.split())
        print('Projeto {}:'.format(p))
        print('Percentual dos juros da aplicacao: {:.2f} %'
              .format(100.0 * (value_return - value_investment) / value_investment))
        print()
