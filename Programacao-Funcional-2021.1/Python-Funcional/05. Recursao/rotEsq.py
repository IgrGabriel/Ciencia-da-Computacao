# IN : Um natural n e uma lista ou string S
# OUT: Lista S rotacionada n vezes à esquerda

def rotEsq(n, lista) :
    if n == 0 :
        return lista
    else :
        return rotEsq(n - 1, lista[1 :] + [lista[0]])


print(rotEsq(0, ['a', 's', 'd', 'f', 'g']))
print(rotEsq(1, ['a', 's', 'd', 'f', 'g']))
print(rotEsq(3, ['a', 's', 'd', 'f', 'g']))
print(rotEsq(4, ['a', 's', 'd', 'f', 'g']))
