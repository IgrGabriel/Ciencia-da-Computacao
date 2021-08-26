# retorna o menor valor entre três números
def min3(a, b, c):
    if a < b and b <= c:
        return a
    elif b < a and a <= c:
        return b
    elif c < a and a <= b:
        return c
    else:
        return a

print(min3(1, 2, 3))
print(min3(2, 1, 3))
print(min3(3, 4, 2))
print(min3(2, 5, 4))