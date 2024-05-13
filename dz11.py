'''
# 1 способ
class MealyError(Exception):
    pass


class MealyStateMachine:
    def __init__(self):
        self.state = 'A'

    def slip(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 5
        raise MealyError('slip')

    def sweep(self):
        if self.state == 'A':
            self.state = 'G'
            return 1
        if self.state == 'E':
            self.state = 'E'
            return 8
        if self.state == 'B':
            self.state = 'F'
            return 4
        raise MealyError('sweep')

    def reset(self):
        if self.state == 'B':
            self.state = 'B'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('reset')


def main():
    return MealyStateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
        assert output is None


def test():
    o = main()
    raises(o.reset, MealyError)
    assert o.slip() == 0
    assert o.reset() == 3
    assert o.slip() == 2
    raises(o.reset, MealyError)
    assert o.slip() == 5
    raises(o.sweep, MealyError)
    assert o.reset() == 6
    assert o.sweep() == 8
    assert o.reset() == 7
    raises(o.slip, MealyError)
    raises(o.sweep, MealyError)
    assert o.reset() == 9

    o = main()
    assert o.sweep() == 1

    o = main()
    raises(o.reset, MealyError)
    assert o.slip() == 0
    assert o.sweep() == 4
    assert o.reset() == 9


test()
'''

# 2 способ
result = []


class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def slip(self):
        match self.state:
            case 'A':
                self.state = 'B'
                result.append(0)
                return 0
            case 'B':
                self.state = 'C'
                result.append(2)
                return 2
            case 'C':
                self.state = 'D'
                result.append(5)
                return 5
            case _:
                raise MealyError('slip')

    def sweep(self):
        match self.state:
            case 'A':
                self.state = 'G'
                result.append(1)
                return 1
            case 'E':
                self.state = 'E'
                result.append(8)
                return 8
            case 'B':
                self.state = 'F'
                result.append(4)
                return 4
            case _:
                raise MealyError('sweep')

    def reset(self):
        match self.state:
            case 'B':
                self.state = 'B'
                result.append(3)
                return 3
            case 'D':
                self.state = 'E'
                result.append(6)
                return 6
            case 'E':
                self.state = 'F'
                result.append(7)
                return 7
            case 'F':
                self.state = 'G'
                result.append(9)
                return 9
            case _:
                raise MealyError('reset')


class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name
        global result


def main():
    return MealyMachine()


def test():
    global result
    o = main()
    try:
        o.reset()
    except MealyError:
        pass
    o.slip()
    o.reset()
    o.slip()
    try:
        o.reset()
    except MealyError:
        pass
    o.slip()
    try:
        o.sweep()
    except MealyError:
        pass
    o.reset()
    o.sweep()
    o.reset()
    try:
        o.slip()
    except MealyError:
        pass
    try:
        o.sweep()
    except MealyError:
        pass
    o.reset()

    result = []
    o = main()
    o.sweep()

    result = []
    o = main()
    try:
        o.reset()
    except MealyError:
        pass
    o.slip()
    o.sweep()
    o.reset()


    return result






'''
# 3 способ
class MealyError(Exception):
    def __init__(self, method_name):
        super().__init__
        (f"Method '{method_name}' not implemented for current state")
        self.method_name = method_name


class MealyStateMachine:
    def __init__(self):
        self.state = 'A'
        self.transitions = {
            'A': {'slip': ('B', 0), 'sweep': ('G', 1)},
            'B': {'slip': ('C', 2), 'reset': ('B', 3), 'sweep': ('F', 4)},
            'C': {'slip': ('D', 5)},
            'D': {'reset': ('E', 6)},
            'E': {'reset': ('F', 7), 'sweep': ('E', 8)},
            'F': {'reset': ('G', 9)},
            'G': {}
        }

    def slip(self):
        if 'slip' in self.transitions[self.state]:
            next_state, value = self.transitions[self.state]['slip']
            self.state = next_state
            return value
        else:
            raise MealyError('slip')

    def reset(self):
        if 'reset' in self.transitions[self.state]:
            next_state, value = self.transitions[self.state]['reset']
            self.state = next_state
            return value
        else:
            raise MealyError('reset')

    def sweep(self):
        if 'sweep' in self.transitions[self.state]:
            next_state, value = self.transitions[self.state]['sweep']
            self.state = next_state
            return value
        else:
            raise MealyError('sweep')


def main():
    return MealyStateMachine()


def test():
    test_cases = [
        ["slip", "reset", "slip", "reset",
         "slip", "reset", "sweep", "sweep", "reset", "reset"],
        ["slip", "reset", "reset", "slip", "slip",
         "reset", "sweep", "sweep", "sweep", "reset", "reset"],
        ["reset", "sweep"],
        ["slip", "sweep", "reset"],
        ["reset", "slip", "reset", "sweep", "slip", "sweep", "reset"]
    ]

    results = [
        [0, 3, 2, 'MealyError', 5, 6, 8, 8, 7, 9],
        [0, 3, 3, 2, 5, 6, 8, 8, 8, 7, 9],
        ['MealyError', 1],
        [0, 4, 9],
        ['MealyError', 0, 3, 4, 'MealyError', 'MealyError', 9]
    ]

    for idx, test_case in enumerate(test_cases):
        o = main()
        expected_results = []
        for call in test_case:
            try:
                method_name = call.split()[0]
                method = getattr(o, method_name)
                result = method()
                expected_results.append(result)
            except MealyError:
                expected_results.append("MealyError")

        assert results[idx] == expected_results


test()  # Автоматически запускаем тестирование
'''






