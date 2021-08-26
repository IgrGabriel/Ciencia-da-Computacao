# Lista das chaves que xs e ys possuem em comum

def intersec(xs, ys) :
    return [x for x in xs if x in ys]

print(intersec([3], [3]))
print(intersec([3,4,1], [1,4,3]))
print(intersec([3,6,5,7], [9,7,5,1,3,6]))
print(intersec([3,6,5,7], [9,7,5,1,3]))