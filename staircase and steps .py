

def aFiboLikeFuntion(n, steps):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1

    for i in range(1, n+1):
        for step in steps:
            s = 0
            if i-step >= 0:
                s += cache[i-step]
            cache[i] += s

    return cache[n]


def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

steps = [1,3,5]

print(aFiboLikeFuntion(1, steps))
print(aFiboLikeFuntion(2, steps))
print(aFiboLikeFuntion(3, steps))
print(aFiboLikeFuntion(4, steps))
print(aFiboLikeFuntion(5, steps))
print(aFiboLikeFuntion(6, steps))
print(aFiboLikeFuntion(7, steps))
print(aFiboLikeFuntion(8, steps))
print(aFiboLikeFuntion(9, steps))
print(aFiboLikeFuntion(10, steps))
