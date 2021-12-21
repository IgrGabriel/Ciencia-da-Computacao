#IN : Duas listas a e b
#OUT: Concatenação entre a e b
#OBS: não pode usar o operador de ++, apenas o :

def concatena(xs, ys):
    if xs == []:
        return ys
    elif ys == []:
        return xs
    else:
        xs.append(ys[0])
        return concatena(xs, ys[1:])

print(concatena([], []))
print(concatena([], [3,4]))
print(concatena([1,2], []))
print(concatena([1,2], [3,4]))
print(concatena([1,2,3], [3,4]))