import math


def main(Ф):
    K = {ф for ф in Ф if (ф > -84 or ф < 49)}
    A = {math.ceil(ф/8) for ф in Ф if (ф < 84) != (ф >= -48)}
    X = {math.floor(a/2) + a % 2 for a in A if a > -32 and a < 49}
    v = len(K.union(X)) - sum(abs(к) + x for к in K for x in X)
    return v

# Примеры использования функции
print(main({-32, -31, -28, 45, -81, 84, -43, -10, -73, 31}))  # Должно вывести -1331
print(main({38, -24, -55, 10, -86, -51, -82, 79, 28, -1}))    # Должно вывести -816
