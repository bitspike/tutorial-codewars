import re

def calc(expression):
    # Tokenize
    tokens = []
    token = ''
    state = 'num' if expression[0].isnumeric() else 'op'
    for c in expression:
        if c is ' ':
            continue
        if state == 'num':
            if c.isnumeric():
                token += c
            else:
                tokens.append(float(token))
                token = ''
                state = 'op'
        if state == 'op':
            if not c.isnumeric():
                tokens.append(c)
            else:
                token = c
                state = 'num'
    if state == 'num':
        tokens.append(float(token))

    # Parse
    context = [[]]
    for t in tokens:
        if t == '(':
            context.append([])
        elif t == ')':
            paren = context.pop()
            context[-1].append(calc_simple(paren))
        else:
            context[-1].append(t)
    parsed = context[-1]
    
    return calc_simple(parsed)


def calc_simple(parsed_expression):
    print(parsed_expression, end=">>")
    
    # Evaluate - sings
    for i in range(len(parsed_expression)-1,-1,-1):
        if (parsed_expression[i] == '-' and i==0) or \
           (parsed_expression[i] == '-' and i>0 and type(parsed_expression[i-1]) is str and parsed_expression[i-1] in '*/'):
            parsed_expression[i+1] = -parsed_expression[i+1]
            del parsed_expression[i]
        elif (parsed_expression[i] == '-' and i>0 and type(parsed_expression[i-1]) is str and parsed_expression[i-1] in '+-'):
            parsed_expression[i-1] = '+' if parsed_expression[i-1] == '-' else '-'
            del parsed_expression[i]
    print(parsed_expression)

    parsed_expression.reverse()

    # Evaluate / operations
    for i in range(len(parsed_expression)-1,-1,-1):
        if parsed_expression[i] == '/':
            parsed_expression[i-1] = parsed_expression[i+1] / parsed_expression[i-1]
            del parsed_expression[i:i+2]

    # Evaluate * operations
    for i in range(len(parsed_expression)-1,-1,-1):
        if parsed_expression[i] == '*':
            parsed_expression[i-1] = parsed_expression[i-1] * parsed_expression[i+1]
            del parsed_expression[i:i+2]

    # Evaluate - operations
    for i in range(len(parsed_expression)-1,-1,-1):
        if parsed_expression[i] == '-':
            parsed_expression[i-1] = parsed_expression[i+1] - parsed_expression[i-1]
            del parsed_expression[i:i+2]

    # Evaluate + operations
    for i in range(len(parsed_expression)-1,-1,-1):
        if parsed_expression[i] == '+':
            parsed_expression[i-1] = parsed_expression[i-1] + parsed_expression[i+1]
            del parsed_expression[i:i+2]
            
    print(parsed_expression, end="\n\n")
    return parsed_expression[0]