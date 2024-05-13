from math import floor, sin, cos


def main(x: int) -> float: # 3 способ
    conditions = {
        x < 38: lambda x: (11 + 30 * x ** 3) ** 7,
        38 <= x < 66: lambda x: floor((x + x ** 3 + 98) ** 3),
        66 <= x < 89: lambda x:
        (sin(x)) ** 2 + ((x ** 3) / (67)) + (cos(x)) ** 4,
    }

    for condition, expression in conditions.items():
        if condition:
            return expression(x)

    return 28 * (19 * x) ** 7



def main(x): # 2 способ
    return ((11 + 30 * x ** 3) ** 7 if x < 38 else
            (floor((x + x ** 3 + 98) ** 3) if 38 <= x < 66 else
             ((sin(x)) ** 2 + ((x ** 3) /
              (67)) + (cos(x)) ** 4 if 66 <= x < 89 else
              28 * (19 * x) ** 7)))


def main(x: int) -> float: # 1 способ
    if x < 38:
        return (11 + 30 * x ** 3) ** 7
    elif x >= 38 and x < 66:
        return floor((x + x ** 3 + 98) ** 3)
    elif x >= 66 and x < 89:
        return (sin(x)) ** 2 + ((x ** 3) / (67)) + (cos(x)) ** 4
    else:
        return 28 * (19 * x) ** 7

print(main(104))