# https://codechick.io/challenges/318



def XO(txt):
    counter_x = 0
    counter_o = 0
    for i in txt.lower():
        if i == 'x':
            counter_x += 1
        elif i == 'o':
            counter_o += 1
    return counter_x == counter_o