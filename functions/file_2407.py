def summator(a, b):
    print(a + b)


# summator(4, 5)
# summator(2, 3)
# summator(-2, 3)

# --------------------------
nums: list = [10, 20, 30, 40, 50]
fruits: list = ['Яблоко', 'Апельсин', 'Бананы', 'Манго']


# print(nums)

# --------------------------


def my_print(data: list):
    for elem in data:
        print(elem, end='; ')
    print()


# my_print(nums)
# my_print(fruits)

# --------------------


def custom_separator(data: list, my_sep: str = ' '):
    for elem in data:
        print(elem, end=my_sep)
    print()


custom_separator(nums, my_sep=' | ')
custom_separator(fruits)

# --------------------

# Аннотация типа
x: int = 10
line: str = 'Hello, World!'

result: float | int = 3 * 4
# print(result)
