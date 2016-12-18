def merge(a1, a2):
    ma = []
    i1, i2 = 0, 0
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            ma.append(a1[i1])
            i1 += 1
        else:
            ma.append(a2[i2])
            i2 += 1
    while i1 < len(a1):
        ma.append(a1[i1])
        i1 += 1

    while i2 < len(a2):
        ma.append(a2[i2])
        i2 += 1

    return ma
