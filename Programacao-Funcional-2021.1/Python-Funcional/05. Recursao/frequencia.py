# IN : Lista u e valor x
# OUT: O total de ocorrências de x em u

# frequencia com filter
def frequencia1(n, lista) :
    if lista == [] :
        return 0
    else :
        return len(list(filter(lambda x : x == n, lista)))


# frequencia com compreensão de lista
def frequencia2(n, lista) :
    return len([x for x in lista if x == n])


# frequencia com recursão
def frequencia3(n, lista) :
    if lista == [] :
        return 0
    elif lista[0] == n :
        return 1 + frequencia3(n, lista[1 :])
    else :
        return 0 + frequencia3(n, lista[1 :])


print("F1:", frequencia1(1, []), "F2:", frequencia2(1, []), "F3:", frequencia3(1, []))
print("F1:", frequencia1(4, [4]), "F2:", frequencia2(4, [4]), "F3:", frequencia3(4, [4]))
print("F1:", frequencia1(4, [5]), "F2:", frequencia2(4, [5]), "F3:", frequencia3(4, [5]))
print("F1:", frequencia1(4, [4, 4]), "F2:", frequencia2(4, [4, 4]), "F3:", frequencia3(4, [4, 4]))
print("F1:", frequencia1(2, [4, 4]), "F2:", frequencia2(2, [4, 4]), "F3:", frequencia3(2, [4, 4]))
print("F1:", frequencia1(5, [4, 5, 2, 1, 5, 5, 9]), "F2:", frequencia2(5, [4, 5, 2, 1, 5, 5, 9]), "F3:",
      frequencia3(5, [4, 5, 2, 1, 5, 5, 9]))
