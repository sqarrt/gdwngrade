import random as rnd
import numpy

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
        ort.append(diff(lambda x: f(*(args[:i]+(x, )+args[i+1:])), args[i]))
    return tuple(ort)


def minimum(f, *args):
    point = list(args)
    gr = grad(f, *point)
    k = 1
    while sum(gr) > EPS or k < TIMES:
        point = [p - ALPHA * (g + rnd.random()*g*ALPHA) for p, g in zip(point, gr)]
        gr = grad(f, *point)
        k = k + 1
    return point


def maximum(f, *args):
    point = list(args)
    gr = grad(f, *point)
    k = 1
    while sum(gr) > EPS or k < TIMES:
        point = [p + ALPHA * (g + rnd.random()*g*ALPHA) for p, g in zip(point, gr)]
        gr = grad(f, *point)
        k = k + 1
    return point


print(maximum(numpy.cos, 4))
