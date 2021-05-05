def func(*args):
    sum = 0
    for args in args:
        sum += args
    print(sum)


func(10, 25, 35, 60)


def func(**kwargs):
    print(kwargs)


func(Muttu='Fart lord', MindLevel='DumbAss')


def func(*sample, **dummy):
    print(sample)
    print(dummy)


func(45, 569, TT='0.-1')
