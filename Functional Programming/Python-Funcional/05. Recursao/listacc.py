# IN : Lista u de inteiros
# OUT: Versão v acumulativa de u. Na versão acumulativa a k-ésima chave,
# vk é determinada somando-se as todas as chaves de u até a posição k.

def listacc(lista) :
    if lista == [] :
        return []
    else :
        return listacc(lista[:len(lista) - 1]) + [sum(lista)]


print(listacc([]))
print(listacc([1]))
print(listacc([1, 3, 4]))
print(listacc([4, 3, 1, 1]))
print(listacc([1, 2, 3, 4]))
