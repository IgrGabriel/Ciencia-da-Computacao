#IN : Lista de inteiros positivos, u
#OUT: Tupla de duas listas, (A,B), onde A e B são respectivamente compostos pelos números que passam no predicado e os que não passam
def odd(x):
    if x % 2 == 1:
        return x

def menor5(x):
    if x < 5:
        return  x

def splitints(lista):
    xs = list(filter(lambda x: odd(x), lista))
    ys = list(filter(lambda x: not odd(x), lista))
    return (xs, ys)

def splitints2(lista):
    xs = list(filter(lambda x: menor5(x), lista))
    ys = list(filter(lambda x: not menor5(x), lista))
    return (xs, ys)

print(splitints([1,2,3,4,5,6,7]))
print(splitints2([2,4,6,1,1,7]))