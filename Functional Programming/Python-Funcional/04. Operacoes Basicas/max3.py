def max3 (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return a

print(max3(6,2,4))
print(max3(6,7,4))
print(max3(6,7,9))
print(max3(5,2,5))
