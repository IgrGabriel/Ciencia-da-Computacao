# Função que recebe uma lista e retorna a quantidade de elementos negativos dela
def countNeg(lista):
    return len([x for x in lista if x < 0])

print("Qtd negativos Lista 1:", countNeg([]))
print("Qtd negativos Lista 2:",countNeg([1,2,3,4,5]))
print("Qtd negativos Lista 3:",countNeg([1,-1,2,-3,4]))
print("Qtd negativos Lista 4:",countNeg([2,-2]))
print("Qtd negativos Lista 5:",countNeg([1,-1]))
print("Qtd negativos Lista 6:",countNeg([1,-3,-4,3,4,-5]))