from collections import deque
parentheses = deque(input())
opened_parentheses = deque()

opening = ["[", "{", "("]
pairs = {"]": "[", "}": "{", ")": "("}
unbalanced = None

while parentheses:
    current_ch = parentheses.popleft()
    if current_ch in opening:
        opened_parentheses.append(current_ch)
    elif opened_parentheses:
        if pairs[current_ch] == opened_parentheses[-1]:
            opened_parentheses.pop()
    else:
        unbalanced = True
        break

if not unbalanced and len(parentheses) == 0 and len(opened_parentheses) == 0:
    print("YES")
else:
    print("NO")