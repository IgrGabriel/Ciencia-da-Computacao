# IN : Natural n e lista u
# OUT: Lista com os n menores elementos de u na ordem que aparecem em u

def delete(n, xs) :
    if xs == [] :
        return []
    elif xs[0] == n :
        return xs[1 :]
    else :
        return [xs[0]] + delete(n, xs[1 :])


def menores(n, lista) :
    if n >= len(lista) :
        return lista
    else :
        return menores(n, delete(max(lista), lista))


print(menores(0, [6, 2, 2, 4, 9]))
print(menores(1, [6, 2, 2, 4, 9]))
print(menores(3, [5, 5, 5]))
print(menores(2, [5, 5, 2, 5]))
print(menores(2, [6, 2, 2, 4, 9]))
print(menores(2, [6, 2, 3, 4, 9]))
print(menores(3, [6, 2, 3, 4, 9]))
print(menores(4, [6, 2, 3, 4, 9]))
print(menores(5, [6, 2, 3, 4, 9]))
print(menores(4, [3, 1, 2]))
print(menores(3, [5, 3, 1, 9, 7, 2]))
