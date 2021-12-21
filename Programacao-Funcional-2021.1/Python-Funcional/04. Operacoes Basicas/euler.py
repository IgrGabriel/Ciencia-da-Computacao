# Calcular a soma de todos os numeros de 1 ate n que sao multiplos de 3 ou de 5

def euler1(n):
    return sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0,list(range(1, n)))))

print(euler1(3))
print(euler1(4))
print(euler1(5))
print(euler1(6))
print(euler1(10))
print(euler1(1000))
