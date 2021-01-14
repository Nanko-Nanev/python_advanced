from collections import deque
parentheses = deque(input())
unbalanced = 0

while parentheses:
    first_ch = parentheses.popleft()
    last_ch = parentheses.pop()

    if (first_ch == "{" and last_ch == "}") or (first_ch == "}" and last_ch == "{"):
        pass
    elif (first_ch == "(" and last_ch == ")") or (first_ch == ")" and last_ch == "("):
        pass
    elif (first_ch == "[" and last_ch == "]") or (first_ch == "]" and last_ch == "["):
        pass
    else:
        unbalanced = 1
        print("NO")
        break

if unbalanced == 0:
    print("YES")
