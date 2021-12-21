# IN : Lista u e valor x
# OUT: True se x ocorre exatamente uma vez em u e false do contrário

def unico(n, lista) :
    return len([x for x in lista if n == x]) == 1


print(unico(2, [2]))
print(unico(2, [3, 1]))
print(unico(2, [1, 2, 3, 2]))
