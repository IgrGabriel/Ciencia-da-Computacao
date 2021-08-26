#import functools

# Função que computa o número de elementos negativos em uma lista

# countNeg x = length (filter (\x -> x < 0) x)

# Adicionando elementos em uma lista
lista = []

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

print("Elementos adicionados: ", lista)

# Modificando os elementos da lista
lista[1] = 4
lista[3] = 8
lista[2] = 7
lista[0] = 2

print("\nElementos modificados: ", lista)

# Adicionado elementos de uma lista em outra lista com extend
bolo = ['farinha de trigo', 'ovo', 'leite', 'manteiga']
bolo.append(['açucar', 'fermento'])
print(bolo)
bolo.extend(['glacê', 'pasta americana'])
print(bolo)

# Inserindo elementos em uma posiçao especifica da lista
lista = ['P', 'T', 'H', 'N']
lista.insert(1, "Y")
lista.insert(4, "O")

print("\n", lista)

# Removendo elementos da lista
lista = ['A', 'S', 'C', 'E', 'N', 'D', 'E', 'R']
print("\nLista original: ", lista)

lista.remove("S")
print("Removendo um elemento: ", lista)

# Remover um elemento em uma posicao especifica
lista = ['A', 'S', 'C', 'E', 'N', 'D', 'E', 'N','T','E']
print("\nLista original: ", lista)

del lista[1]
print("Removendo um elemento: ", lista,"\n")

# Deixando os frutas (elementos) da lista no plural
# Criando uma lista dentro de um for.
frutas = ['laranja', 'banana', 'abacate', 'manga']
plurais_frutas = []
for fruta in frutas:
    plural = fruta + 's'
    plurais_frutas += [plural]
print(plurais_frutas)
# ----------
lista = [1, [2, [3, [4]]], 5]
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatriz impressa de outra forma:")
for lista in matriz :
    for elemento in lista :
        print(elemento, end=' ')
    print()

# Convertendo um intervalo em uma lista.
#  print(list(range(inicio, fim, passo)))
print("\nGerando uma lista: ")
print(list(range(0, 10, 1)))

# Ordenando listas.
lista = [7, 25, 2, 3, 30, 7, 80, 100, -1, 15]
print("\nLista não ordenada: ", lista)

lista.sort()
print("Lista ordenada: ", lista)

lista.sort(reverse=True)
print("Lista ordenada em ordem decrescente: ", lista)

# Ordenando listas.
lista = [7, 2, 3, 7, -1, 9]
print("\nLista original antes da ordenação: ", lista)

lista_ordenada = sorted(lista)
print("Lista ordenada: ", lista_ordenada)

print("A lista original permanece inalterada: ", lista, "\n")

# Converte uma string em uma lista.
s = list("Ordem e Progresso")
print(s)

# Converte uma lista em uma string.
l = ['O', 'r', 'd', 'e', 'm', ' ', 'e', ' ', 'P', 'r', 'o', 'g', 'r', 'e', 's', 's', 'o']
print(''.join(l))

# multiplicando os elementos de uma lista
from functools import reduce
lista = [1,2,3,4,5]
mult = reduce(lambda x, y : x * y, lista)

print(mult)