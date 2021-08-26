def uniao(xs, ys) :
    xs.extend([y for y in ys if not y in xs])
    return xs

print(uniao([4,5], [1]))
print(uniao([4,5], [4,2,5]))
print(uniao([1,2,3], [4,5,6]))
