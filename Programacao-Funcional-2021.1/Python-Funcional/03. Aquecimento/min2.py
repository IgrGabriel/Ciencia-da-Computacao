# retorna o menor valor entre dois elementos
def min2(a,b):
    if a > b:
        return b
    else:
        return a

print("O menor elemento é:",min2(3, 4))
print("O menor elemento é:",min2(4, 1))
print("O menor elemento é:",min2(2, 2))
print("O menor elemento é:",min2(4, -1))