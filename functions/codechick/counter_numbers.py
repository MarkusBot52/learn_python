# https://codechick.io/challenges/317


def num_of_digits(num):
    numbers = '1234567890'
    num_1 = str(num)
    counter = 0
    for i in num_1:
        if i in numbers:
            counter += 1
    return counter