def diff(f, p):
    delta = [10**(-a) for a in range(3, 9)]
    value = [(f(p + a) - f(p - a))/(2*a) for a in delta]
    return sum(value)/len(value)


def f(*args):
    res = args[0]**2
    for a in args:
        if a**2 != res:
            res = res*a
    return res


def grad(f, *args):
    ort = []
    for i, a in enumerate(args):
        temp = list(args)
        ort.append(diff(lambda x: f(*(temp[:i]+[(lambda x: x)(x), ]+temp[i+1:])), args[i]))
    return tuple(ort)


v = grad(f, 1, 2, 1, 3)

print(v, sum(v))




