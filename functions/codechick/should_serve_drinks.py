# https://codechick.io/challenges/85


def should_serve_drinks(age, on_break):
    if (age >= 18) and (not on_break):
        return True
    else:
        return False