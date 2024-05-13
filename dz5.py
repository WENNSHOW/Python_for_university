
'''
import math  


def main(y, x, z, n=7, i=1, res=0):  # 4 способ
    if i > n:
        return 4 * res
    else:
        res += 18 * math.tan((y[math.ceil(i / 4) - 1]) ** 2 +
                             16 * (x[i - 1]) ** 3 +
                             71 * z[n + 1 - i - 1]) ** 6
        return main(y, x, z, n, i+1, res)
'''


'''
def main(y, x, z):  # 3 способ
    n = 7
    res = 0
    i = 1
    while i <= n:
        res += 18 * math.tan((y[math.ceil(i / 4) - 1]) ** 2 +
                             16 * (x[i - 1]) ** 3 +
                             71 * z[n + 1 - i - 1]) ** 6
        i += 1
    return 4 * res
'''

'''
import math
# 3 способ

def main(y, x, z):   # 2 способ
    n = 7
    return 4 * sum(18 * math.tan((y[math.ceil(i / 4) - 1]) ** 2 +
                                 16 * (x[i - 1]) ** 3 +
                                 71 * z[n + 1 - i - 1]) ** 6
                   for i in range(1, n + 1))
'''





'''
import math


def main(y, x, z):  # 1 способ
    n = 7
    res = 0
    for i in range(1, n + 1):
        res += 18 * math.tan((y[math.ceil(i / 4) - 1]) ** 2 +
                             16 * (x[i - 1]) ** 3 +
                             71 * z[n + 1 - i - 1]) ** 6
    return 4 * res
'''

print(main([-0.16, 0.94, -0.27, -0.81, -0.39, -0.18, 0.51],
[-0.3, 0.93, 0.19, 0.12, 0.41, -0.03, -0.55],
[0.48, -0.23, -0.51, 0.01, 0.18, -0.92, -0.33]))