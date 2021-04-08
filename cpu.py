instructions = {}
accumulator = 0


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


instructions['calc'] = calc

def execute():
    global accumulator
    with open('statements.txt') as f:
        for line in f:
            instruction, params = line.split(' ', 1)
            assert instruction in instructions
            accumulator += instructions[instruction](params)


if __name__ == '__main__':
    execute()
    print(accumulator)
