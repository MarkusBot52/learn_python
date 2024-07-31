# https://codechick.io/challenges/312


def halloween(dt):
    data: list = dt.split('/')
    if data[1] == '10' and data[2] == '31':
        return 'Bonfire toffee'
    else:
        return 'toffee'



# Ошибок нет, тесты прошли.