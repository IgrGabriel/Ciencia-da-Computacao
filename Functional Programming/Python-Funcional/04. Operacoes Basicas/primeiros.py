# retorna a lista menos o útimo elemento
def primeiros(lista):
    return lista[0:(len(lista)-1)]

print(primeiros([1]))
print(primeiros([1,2]))
print(primeiros([1,2,3,4]))