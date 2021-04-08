# for the purposes of this exercise, line numbers are 1-indexed


instructions = {}
pc = 1
executedStatements = set()


with open('statements.txt') as f:
    statements = f.readlines()


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


def execute():
    global pc
    while True:
        executeLine(pc)
        pc += 1


def executeLine(lineNumber):
    statement = getStatement(lineNumber)
    if statement in executedStatements:
        raise SystemExit
    executedStatements.add(statement)
    executeStatement(statement)


def executeStatement(statement):
    instruction, params = statement.split(' ', 1)
    assert instruction in instructions
    return instructions[instruction](params)


def getStatement(lineNumber):
    return statements[lineNumber - 1].rstrip()


def goto(params):
    global pc
    params = params.split(' ')
    if len(params) == 1:
        pc = int(params[0])
    else:
        pc = int(executeStatement(' '.join(params)))
    pc -= 1 # will be incremented after this instruction executes


instructions['calc'] = calc
instructions['goto'] = goto


if __name__ == '__main__':
    try:
        execute()
    except SystemExit:
        pass
    print(f'Duplicate statement: {getStatement(pc)}')
    print(f'Line number (1 indexed): {pc}')
