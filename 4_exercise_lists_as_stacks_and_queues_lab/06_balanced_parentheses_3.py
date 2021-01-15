parentheses_data = list(input())
parentheses = []

for i in range(len(parentheses_data)):
    if parentheses_data[i] in '([{':
        parentheses.append(parentheses_data[i])
    if parentheses:
        if parentheses_data[i] == ')' and parentheses[-1] == '(':
            parentheses.pop()
        elif parentheses_data[i] == ']' and parentheses[-1] == '[':
            parentheses.pop()
        elif parentheses_data[i] == '}' and parentheses[-1] == '{':
            parentheses.pop()
    else:
        parentheses.append(parentheses_data[i])
        break

if not len(parentheses) == 0:
    print('NO')
else:
    print('YES')