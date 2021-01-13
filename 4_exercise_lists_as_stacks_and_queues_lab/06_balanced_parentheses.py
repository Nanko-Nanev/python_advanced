from collections import deque
parentheses = deque(input())
balanced = False

while parentheses:
    first_ch = parentheses.popleft()
    last_ch = parentheses.pop()

    if first_ch == "{":
        if last_ch == "}":
            balanced = True
        else:
            balanced = False
            break
    elif first_ch == "(":
        if last_ch == ")":
            balanced = True
        else:
            balanced = False
            break
    elif first_ch == "[":
        if last_ch == "]":
            balanced = True
        else:
            balanced = False
            break
    else:
        break

if balanced:
    print("YES")
else:
    print("NO")