# função que retorna o tamanho de uma lista sem usar a função len
def tamanho(lista) :
    return sum(map(lambda x : 1, lista))

print(tamanho([1, 2, 3, 4, 5, 6]))
