# Dado três valores, retorna quantos dos três são iguais
def iguais(a, b, c):
    if a == b and b == c:
        return 3
    elif a != b and b != c and c != a:
        return 0
    else:
        return 2

print(iguais(2,2,2) == 3)
print(iguais(2,2,3) == 2)
print(iguais(2,3,2) == 2)
print(iguais(2,1,1) == 2)
print(iguais(3,2,1) == 0)