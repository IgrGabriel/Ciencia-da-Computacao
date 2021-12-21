l = [2,5,4,7,9,6]

# retorna um lista formada pelos n elementos finais de xs
def final(n, xs):
    y = len(xs)
    x = y - n
    return xs[x:y]

print(final(3, l))
print(final(2, l))
print(final(1, l))