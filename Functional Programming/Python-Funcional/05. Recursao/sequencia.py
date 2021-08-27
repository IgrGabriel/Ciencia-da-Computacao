# IN : Dois números naturais n e m
# OUT: Lista [m, m+1, m+2, ..., m+n-1]

def sequencia(n, m) :
    if n == 0 :
        return []
    elif n == 1 :
        return [m]
    else :
        return list(map(lambda x : x + m, list(range(n))))


print(sequencia(0, 2))
print(sequencia(1, 2))
print(sequencia(3, 5))
print(sequencia(4, 4))
