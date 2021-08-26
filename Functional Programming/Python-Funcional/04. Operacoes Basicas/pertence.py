# caso elem pertença a lista retorna True se não False
def pertence(elem, lista) :
    xs = [x for x in lista if x == elem]
    return xs != []

print(pertence(1, []))
print(pertence(1, [3]))
print(pertence(3, [4]))
print(pertence(1, [3,7,4,2]))
print(pertence(2, [3,7,4,2]))
print(pertence(3, [3,7,4,2]))
print(pertence(7, [3,7,4,2]))