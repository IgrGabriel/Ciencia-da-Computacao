def line(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        inicio = 1 + sum(list(range(1,n)))
        xs = list(range(n))
        return list(map(lambda x: x+inicio, xs))


def triagle(n):
    if n == 0:
        return []
    else:
        return triagle(n-1) + [line(n)]

print(triagle(0))
print(triagle(1))
print(triagle(2))
print(triagle(3))
print(triagle(4))
print(triagle(5))