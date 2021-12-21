from functools import reduce

def fatorial(n) :
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return reduce(lambda x, y : x * y, list(range(1, n + 1)))

print(fatorial(0))
print(fatorial(1))
print(fatorial(5))