# IN : Número x e uma lista u
# OUT: Sublista de u cujos números sejam maiores que x
# OBS: Faça usando filter e CList

# Usando Filter
def maioresQue1(n, lista) :
    return list(filter(lambda x : x > n, lista))


# Usando compreensão de lista
def maioresQue2(n, lista) :
    return [x for x in lista if x > n]


print("M1:", maioresQue1(10, []), "M2:", maioresQue2(10, []))
print("M1:", maioresQue1(10, [11, 9, 12]), "M2:", maioresQue2(10, [11, 9, 12]))
print("M1:", maioresQue1(10, [4, 6, 30, 3, 15, 3, 10, 7]), "M2:", maioresQue2(10, [4, 6, 30, 3, 15, 3, 10, 7]))
