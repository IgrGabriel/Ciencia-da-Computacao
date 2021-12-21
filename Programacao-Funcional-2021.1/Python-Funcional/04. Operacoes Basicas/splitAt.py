# Tupla de duas listas, (A,B), onde A é formada pelas n primeiras chaves da lista e B pelos elementos restantes
def divide(lista, n):
    return (lista[0:n], lista[n:len(lista)])

l = [1,2,3,4]

print(divide(l, 0))
print(divide(l, 1))
print(divide(l, 2))
print(divide(l, 3))
print(divide(l, 4))