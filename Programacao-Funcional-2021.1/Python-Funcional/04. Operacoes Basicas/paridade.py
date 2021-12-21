#IN :  Lista u de valores booleanos
#OUT: Se o total de Trues é ímpar então retorne True e do contrário False

def paridade(lista):
    if lista == []:
        return False
    else:
        qtdTrue = len(list(filter(lambda x: x == True, lista)))
        return qtdTrue % 2 != 0

print(paridade([]))
print(paridade([True,True,False]))
print(paridade([True,False,True,False,True]))
print(paridade([False,True,False]))