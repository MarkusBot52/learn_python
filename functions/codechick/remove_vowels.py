# https://codechick.io/challenges/357


def remove_vowels(txt):
    vowels = 'aeiuo'

    result = ''
    for let in txt:
        if let.lower() not in vowels:
            result += let
    return result
