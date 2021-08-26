def somaImpares(lista):
    return sum ([x for x in lista if x % 2 == 1])

print(somaImpares([2,3,1,5]))
print(somaImpares([1,1,4,2]))
print(somaImpares([3,2,4,6,5,7,8,0,1]))
print(somaImpares([2,3,1,5,2,2]))
print(somaImpares([1,1,1,1]))