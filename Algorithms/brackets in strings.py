
# Closed Brackets Stack Analyzer
def check_bracket(array):
    stack = []
    ok = True

    for i in array:
        if i in '([{':
            stack.append(i)

        elif i in ')]}':
            if not stack:
                ok = False
                break

            open_bracket = stack.pop()
            if open_bracket == '(' and i == ')':
                continue
            if open_bracket == '[' and i == ']':
                continue
            if open_bracket == '{' and i == '}':
                continue
            ok = False
            break

    if ok and not stack:
        print('ok')
    else:
        print('brackets not ok')


first = '({)}}}}'
check_bracket(first)

