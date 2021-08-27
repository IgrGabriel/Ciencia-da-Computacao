# IN : Um natural n e uma lista ou string S
# OUT: Lista S rotacionada n vezes à direita

def rotDir(n, lista):
    if n == 0 :
        return lista
    else :
        return rotDir(n - 1, [lista[len(lista) - 1]] + lista[:len(lista) - 1])


print(rotDir(0, ['a', 's', 'd', 'f', 'g']))
print(rotDir(1, ['a', 's', 'd', 'f', 'g']))
print(rotDir(2, ['a', 's', 'd', 'f', 'g']))
print(rotDir(3, ['a', 's', 'd', 'f', 'g']))
print(rotDir(4, ['a', 's', 'd', 'f', 'g']))
print(rotDir(5, ['a', 's', 'd', 'f', 'g']))
