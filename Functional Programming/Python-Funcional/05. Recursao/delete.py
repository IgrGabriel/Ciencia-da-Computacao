#IN : Valor x e lista u
#OUT: Versão de u removendo primeira aparição de x

def delete(n, xs):
    if xs == []:
        return []
    elif xs[0] == n:
        return xs[1:]
    else:
        return [xs[0]] + delete(n, xs[1:])

print(delete(5, []))
print(delete(1, [1]))
print(delete(4, [1,3,4]))
print(delete(3, [4,3,1,3]))
print(delete(5, [1,5,6,9]))