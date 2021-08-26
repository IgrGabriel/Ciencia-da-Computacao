def gangorra(p1, c1, p2, c2):
    if p1 * c1 == p2 * c2:
        return 0
    elif p1 * c1 > p2 * c2:
        return -1
    else:
        return 1

print(gangorra(30, 100, 60, 50))
print(gangorra(40, 40, 38, 60))
print(gangorra(35, 80, 35, 75))
print(gangorra(45, 23, 96, 12))
print(gangorra(74, 12, 65, 48))
print(gangorra(78, 45, 12, 23))