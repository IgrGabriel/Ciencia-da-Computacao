# retorna uma lista sem os elementos dos extremos
def interior(xs):
    return xs[1:len(xs) - 1]

print(interior([1,2]))
print(interior([1,3,2]))
print(interior([2,5,3,7,3]))
print(interior([2,2,2,4]))
print(interior([1,2,3,5,7,8]))