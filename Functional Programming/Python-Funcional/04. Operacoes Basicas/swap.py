#IN : Lista u de tipo arbitrário e dois inteiros p e q que representam posições de elementos de u.
#OUT: Versão de u com os elementos das posições p e q trocados

def swap(u, p, q):
    if u == []:
        return []
    elif len(u) == 1:
        return u
    elif p < q and p < len(u) and q <= len(u):
        aux = u[p]
        u[p] = u[q]
        u[q] = aux
        return u
    else:
        return -1

print(swap([], 0, 5))
print(swap([1], 0, 3))
print(swap([1,3,4], 1, 2))
print(swap([1,2,3,4,5,6], 2, 5))
print(swap([5,6,7,8,9], 0, 3))
