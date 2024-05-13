
'''
def main(n):    # 2 способ
    conditions = {
        n == 0: lambda: 0.25,
        n == 1: lambda: -0.66,
        n >= 2: lambda: main(n - 2) ** 2 - 0.02 - (
            21 + main(n - 1) ** 2 / 55 + main(n - 2) / 40)
    }

    for condition, expression in conditions.items():
        if condition:
            return expression()


'''


'''
def main(n):   # 4 способ
    match n:
        case 0:
            return 0.25
        case 1:
            return -0.66
        case _:
            return main(n - 2) ** 2 - 0.02 - (
                    21 + main(n - 1) ** 2 / 55 + main(n - 2) / 40)

'''



'''
def main(n):    # 3 способ
    if n == 0:
        return 0.25
    elif n == 1:
        return -0.66
    values = [0.25, -0.66]
    for i in range(2, n + 1):
        values.append(values[i - 2] ** 2 - 0.02 - (
            21 + values[i - 1] ** 2 / 55 + values[i - 2] / 40))
    return values[-1]
'''



'''
def main(n): # 5 спосбо
    return 0.25 if n == 0 else (
        -0.66 if n == 1 else main(n - 2) ** 2 - 0.02 - (
            21 + main(n - 1) ** 2 / 55 + main(n - 2) / 40))
'''


'''
def main(n):  # 1 способ
    if n == 0:
        return 0.25
    if n == 1:
        return -0.66
    if n >= 2:
        return (main(n - 2)) ** 2 - 0.02 - (21 + (main(n - 1)) ** 2 / 55 + (main(n - 2)) / 40)
'''
print(main(4))