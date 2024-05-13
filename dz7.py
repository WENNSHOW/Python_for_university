

'''
def x21(x):
    if x[1] == 1995:
        return 7
    if x[1] == 2002:
        return 8
    if x[1] == 1971:
        return 9


def x2(x):
    if x[2] == 2014:
        return x21(x)
    if x[2] == 2019:
        return 10
    if x[2] == 1996:
        return 11


def x13(x):
    if x[3] == 'VHDL':
        return 4
    if x[3] == 'TEA':
        return 5
    if x[3] == 'TOML':
        return 6


def x11(x):
    if x[1] == 1995:
        return 0
    if x[1] == 2002:
        return 1
    if x[1] == 1971:
        return 2


def x1(x):
    if x[2] == 2014:
        return x11(x)
    if x[2] == 2019:
        return 3
    if x[2] == 1996:
        return x13(x)


def main(x):
    if x[0] == 'CMAKE':
        return x1(x)
    if x[0] == 'RHTML':
        return x2(x)
'''

'''
def main(x):
    dict21 = {1995: 7, 2002: 8, 1971: 9}
    dict2 = {2014: dict21[x[1]], 2019: 10, 1996: 11}
    dict13 = {'VHDL': 4, 'TEA': 5, 'TOML': 6}
    dict11 = {1995: 0, 2002: 1, 1971: 2}
    dict1 = {2014: dict11[x[1]], 2019: 3, 1996: dict13[x[3]]}
    dictm = {'CMAKE': dict1[x[2]], 'RHTML': dict2[x[2]]}
    return dictm[x[0]]
'''

'''
def main(x):
    dict_data = {
        ('CMAKE', 2014): {1995: 0, 2002: 1, 1971: 2},
        ('CMAKE', 2019): 3,
        ('CMAKE', 1996): {'VHDL': 4, 'TEA': 5, 'TOML': 6},
        ('RHTML', 2014): {1995: 7, 2002: 8, 1971: 9},
        ('RHTML', 2019): 10,
        ('RHTML', 1996): 11
    }

    match x[0], x[2]:
        case 'CMAKE', 2014:
            return dict_data[('CMAKE', 2014)][x[1]]
        case 'CMAKE', 2019:
            return dict_data[('CMAKE', 2019)]
        case 'CMAKE', 1996:
            return dict_data[('CMAKE', 1996)][x[3]]
        case 'RHTML', 2014:
            return dict_data[('RHTML', 2014)][x[1]]
        case 'RHTML', 2019:
            return dict_data[('RHTML', 2019)]
        case 'RHTML', 1996:
            return dict_data[('RHTML', 1996)]
'''

'''
def x21(x):
    for key in {1995: 7, 2002: 8, 1971: 9}:
        if x[1] == key:
            return {1995: 7, 2002: 8, 1971: 9}[key]


def x2(x):
    for key in {2014: x21(x), 2019: 10, 1996: 11}:
        if x[2] == key:
            return {2014: x21(x), 2019: 10, 1996: 11}[key]


def x13(x):
    for key in {'VHDL': 4, 'TEA': 5, 'TOML': 6}:
        if x[3] == key:
            return {'VHDL': 4, 'TEA': 5, 'TOML': 6}[key]


def x11(x):
    for key in {1995: 0, 2002: 1, 1971: 2}:
        if x[1] == key:
            return {1995: 0, 2002: 1, 1971: 2}[key]


def x1(x):
    for key in {2014: x11(x), 2019: 3, 1996: x13(x)}:
        if x[2] == key:
            return {2014: x11(x), 2019: 3, 1996: x13(x)}[key]


def main(x):
    if x[0] == 'CMAKE':
        return x1(x)
    if x[0] == 'RHTML':
        return x2(x)
'''

class MainSolver:
    def __init__(self, x):
        self.x = x
        self.dict21 = {1995: 7, 2002: 8, 1971: 9}
        self.dict13 = {'VHDL': 4, 'TEA': 5, 'TOML': 6}
        self.dict11 = {1995: 0, 2002: 1, 1971: 2}

    def calculate(self):
        dict2 = {2014: self.dict21[self.x[1]], 2019: 10, 1996: 11}
        dict1 = {2014: self.dict11[self.x[1]],
                 2019: 3, 1996: self.dict13[self.x[3]]}
        dictm = {'CMAKE': dict1[self.x[2]], 'RHTML': dict2[self.x[2]]}
        return dictm[self.x[0]]


def main(x):
    solver = MainSolver(x)
    return solver.calculate()


print(main(['CMAKE', 1995, 1996, 'VHDL']))