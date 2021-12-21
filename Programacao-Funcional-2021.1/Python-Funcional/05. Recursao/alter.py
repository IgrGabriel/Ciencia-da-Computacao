#IN : Inteiro n
#OUT: Lista [1, −1, 2, −2, 3, −3, · · · , n, −n]

def alter(n):
    if n == 0:
        return []
    elif n == 1:
        return [1, -1]
    else:
        return alter(n-1) + [n, -n]

print(alter(1))
print(alter(2))
print(alter(4))