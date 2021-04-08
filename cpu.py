PROMPT = "Enter instruction: "


def calc(params):
    OPERATORS = ('+', '-', 'x', '/')
    params = params.split(' ')
    assert len(params) == 3
    operator = params[0]
    op1 = int(params[1])
    op2 = int(params[2])
    assert operator in OPERATORS
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == 'x':
        return op1 * op2
    elif operator == '/':
        return op1 / op2


if __name__ == '__main__':
    while True:
        print(calc(input(PROMPT)))
