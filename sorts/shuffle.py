from random import randint


def beautiful_shuffle(lst):
    for _ in range(len(lst) // 5):
        i1 = randint(0, len(lst) - 2)
        i2 = randint(i1, len(lst) - 1)
        lst[i1], lst[i2] = lst[i2], lst[i1]
    yield lst
