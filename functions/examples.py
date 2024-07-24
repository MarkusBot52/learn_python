def open_yandex():  # Определение функции
    print('Я Алиса, открываю Яндекс!')
    return 'Hello'


# Вызов(ы) функции
# res_one = open_yandex()
# res_two = open_yandex()
#
# print(res_one, res_two)

# -----------------------


def add_two_nums(x: int, y: int):
    return x + y

# def add_two_nums(x, y):
#     print(x + y)


res_three = add_two_nums(8, 5)
print(res_three)

res_four = add_two_nums(5, 10)
print(res_four)
