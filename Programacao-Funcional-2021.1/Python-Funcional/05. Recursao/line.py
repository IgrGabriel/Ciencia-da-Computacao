# Um triângulo aritmético é construído da seguinte forma:
'''
1
2  3
4  5  6
7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
'''

def line(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        inicio = 1 + sum(list(range(1,n)))
        xs = list(range(n))
        return list(map(lambda x: x+inicio, xs))


print(line(0))
print(line(1))
print(line(2))
print(line(3))
print(line(4))
print(line(5))
print(line(6))