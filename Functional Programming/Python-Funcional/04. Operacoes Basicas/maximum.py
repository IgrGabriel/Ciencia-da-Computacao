def maior(xs):
    max = xs[0]
    for x in xs:
        if max < x:
            max = x
    return max

print(maior([1,2,7,1,5]))