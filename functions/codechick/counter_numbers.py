# https://codechick.io/challenges/317


# №2
# def num_of_digits(num):
#     numbers = '1234567890'
#     num_1 = str(num)
#     counter = 0
#     for i in num_1:
#         if i in numbers:
#             counter += 1
#     return counter


# №2
# def num_of_digits(num):
#     return len(str(num))


# №3
def num_of_digits(num):
    if num == 0:
        return 1

    num = abs(num)
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count
