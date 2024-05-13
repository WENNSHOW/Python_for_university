from functools import reduce # только для 5 способа


def main(b: int, m: int, n: int, x: float) -> float: # 5 способ
    return reduce(
        lambda acc, c: acc + reduce(
            lambda acc_inner, i: acc_inner + reduce(
                lambda acc_innermost, j: acc_innermost +
                ((x ** 3 / 75) + 31 + 82 *
                 (c ** 2 / 40 + j ** 3 + 74 * i) ** 7),
                range(1, b + 1), 0),
            range(1, m + 1), 0),
        range(1, n + 1), 0)






def main(b: int, m: int, n: int, x: float, c=1, i=1, j=1, f=0) -> float: # 4 способ
    if c > n:
        return f
    if i > m:
        return main(b, m, n, x, c + 1, 1, 1, f)
    if j > b:
        return main(b, m, n, x, c, i + 1, 1, f)
    return main(b, m, n, x, c, i, j + 1, f +
                ((x ** 3 / 75) + 31 + 82 *
                 (c ** 2 / 40 + j ** 3 + 74 * i) ** 7))



def main(b, m, n, x): # 3 способ
    f = 0
    c = 1
    while c <= n:
        i = 1
        while i <= m:
            j = 1
            while j <= b:
                f += ((x ** 3 / 75) + 31 + 82 *
                      (c ** 2 / 40 + j ** 3 + 74 * i) ** 7)
                j += 1
            i += 1
        c += 1
    return f






def main(b: int, m: int, n: int, x: float) -> float: # 2 способ
    return sum(((x ** 3 / 75) + 31 + 82 * (c ** 2 / 40 + j ** 3 + 74 * i) ** 7)
               for c in range(1, n + 1)
               for i in range(1, m + 1)
               for j in range(1, b + 1))



def main(b: int, m: int, n: int, x: float) -> float: # 1 способ
    f = 0
    for c in range(1, n + 1):
        for i in range(1, m + 1):
            for j in range(1, b + 1):
                f += ((x ** 3 / 75) + 31 + 82 *
                      (c ** 2 / 40 + j ** 3 + 74 * i) ** 7)

    return f

print(main(4, 6, 2, 0.24))



'''
                f += ((x ** 3 / 75) + 31 + 82 *
                      (c ** 2 / 40 + j ** 3 + 74 * i) ** 7)
'''