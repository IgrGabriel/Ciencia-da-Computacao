# retorna um sublista passanso inicio, fim e a lista
def sublist(init, fim, lista):
    if fim >= 0 and init >= 0:
        return lista[init:fim]
    elif fim < 0 and init >= 0:
        return lista[init:len(lista) + fim]
    else:
        return lista[len(lista) + init:fim]

print(sublist(1, 3, [0,1,2,3,4,5,6,7,8,9,10]))
print(sublist(0, 11, [0,1,2,3,4,5,6,7,8,9,10]))
print(sublist(2, 8, [0,1,2,3,4,5,6,7,8,9,10]))
print(sublist(0, -1, [0,1,2,3,4,5,6,7,8,9,10]))
print(sublist(2, -2, [0,1,2,3,4,5,6,7,8,9,10]))
print(sublist(-10, -1, [0,1,2,3,4,5,6,7,8,9,10]))
print(sublist(-4, -2, [0,1,2,3,4,5]))
