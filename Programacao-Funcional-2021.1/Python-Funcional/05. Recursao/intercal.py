# IN : Duas listas a e b
# OUT: Lista com os elementos de a e b intercalados

def intercal(xs, ys) :
    if xs == ys == [] :
        return []
    elif xs != [] and ys == [] :
        return xs
    elif xs == [] and ys != [] :
        return ys
    else :
        return ([xs[0]] + [ys[0]]) + intercal(xs[1 :], ys[1 :])


print(intercal([1, 2, 3], [7, 8, 9]))
print(intercal([1, 2, 3, 4], [8, 9]))
print(intercal([5], [1, 2, 6]))
