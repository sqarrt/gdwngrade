import random as rnd

ALPHA = 0.1
EPS = 0.0001
TIMES = 1000


def diff(f, p):
    delta = [10**(-a) for a in range(3, 9)]
    value = [(f(p + a) - f(p - a))/(2*a) for a in delta]
    return sum(value)/len(value)


def grad(f, *args):
    ort = []
    for i, a in enumerate(args):
        temp = list(args)
        ort.append(diff(lambda x: f(*(temp[:i]+[(lambda x1: x1)(x), ]+temp[i+1:])), args[i]))
    return tuple(ort)


def minimum(f, *args):
    temp = list(args)
    g = grad(f, *temp)
    k = 1
    while sum(g) > EPS or k < TIMES:
        temp = [a[0] - ALPHA * (a[1] + rnd.random()*a[1]*ALPHA) for a in zip(temp, g)]
        g = grad(f, *temp)
        k = k + 1
    return temp


def maximum(f, *args):
    temp = list(args)
    g = grad(f, *temp)
    k = 1
    while sum(g) > EPS or k < TIMES:
        temp = [a[0] + ALPHA * (a[1] + rnd.random()*a[1]*ALPHA) for a in zip(temp, g)]
        g = grad(f, *temp)
        k = k + 1
    return temp
