# Implementação da função reverse com recursão
# IN : Lista u
# OUT: Lista das chaves de u na ordem inversa

def reverso(lista) :
    if lista == [] :
        return []
    elif len(lista) == 1 :
        return lista
    else :
        return reverso(lista[1 :]) + [lista[0]]


print(reverso([]))
print(reverso([7]))
print(reverso([2, 3]))
print(reverso([1, 2, 3, 4]))
