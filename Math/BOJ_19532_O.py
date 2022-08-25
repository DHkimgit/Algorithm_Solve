a, b, c, d, e, f = map(int, input().split())

for resultx in range(-999, 1000):
    for resulty in range(-999, 1000):
        if (a * resultx + b*resulty == c) and (d * resultx + e*resulty == f):
            print(int(resultx), int(resulty))
