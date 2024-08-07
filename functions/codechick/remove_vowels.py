# https://codechick.io/challenges/357


def remove_vowels(txt):
    vowels = []
    remove = ''
    for i in txt:
        if i !='A' and i !='U' and i !='E' and i !='O' and i !='I' and i !='a' and i !='u' and i !='e' and i !='o' and i !='i':
            vowels.append(i)
    return remove.join(vowels)