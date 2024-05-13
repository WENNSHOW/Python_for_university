import math

def main(x):
    a = (74*x) / (89*(x - x**2/49 - 91*x**3)**2)
    b = x**6 / (17*math.exp(x)**5 - 38*(x**3 + 44*x + 1)**2)
    return a - b

# Пример использования с числами
x_value = 0.11  # Ваше значение x
result = main(x_value)
print("f(x) =", result)

'''
import math

def main(x):
    val = (74*x) / (89*(x - x**2/49 - 91*x**3)**2) - x**6 / (17*math.exp(x)**5 - 38*(x**3 + 44*x + 1)**2)
    return val

# Пример использования с числами
x_value = 0.11  # Ваше значение x
result = main(x_value)
print("f(x) =", result)
import math

def main(x: float) -> float:
    return (74*x) / (89*(x - x**2/49 - 91*x**3)**2) - x**6 / (17*math.exp(x)**5 - 38*(x**3 + 44*x + 1)**2)

# Пример использования с числами
x_value: float = 0.11  # Ваше значение x
result: float = main(x_value)
print("f(x) =", result)

import math

main = lambda x: (74*x) / (89*(x - x**2/49 - 91*x**3)**2) - x**6 / (17*math.exp(x)**5 - 38*(x**3 + 44*x + 1)**2)

# Пример использования с числами
x_value = 0.11  # Ваше значение x
result = main(x_value)
print("f(x) =", result)

import math

def create_f():
    return lambda x: (74*x) / (89*(x - x**2/49 - 91*x**3)**2) - x**6 / (17*math.exp(x)**5 - 38*(x**3 + 44*x + 1)**2)

# Создаем функцию f с помощью лямбда-выражения
main = create_f()

# Пример использования с числами
x_value = 0.11  # Ваше значение x
result = main(x_value)
print("f(x) =", result)
'''