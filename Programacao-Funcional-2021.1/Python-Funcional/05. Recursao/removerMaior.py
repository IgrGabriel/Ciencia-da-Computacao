# IN : Uma lista u
# OUT: A lista sem o maior elemento

def removerMaior(lista) :
    if len(lista) == 1 or lista == [] :
        return []
    else :
        return list(filter(lambda x : x < max(lista), lista))


print(removerMaior([1]))
print(removerMaior([1, 3]))
print(removerMaior([1, 3, 5]))
print(removerMaior([1, 3, 5, 2]))
