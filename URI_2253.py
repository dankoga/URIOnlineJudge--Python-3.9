while True:
    try:
        password = input()
    except EOFError:
        break
    if 6 <= len(password) <= 32 and password.isalnum() \
        and any([c.isupper() for c in password]) \
        and any([c.islower() for c in password]) \
        and any([c.isnumeric() for c in password]):
        print('Senha valida.')
    else:
        print('Senha invalida.')
