n = int(input())
user_names = set([])

for _ in range(n):
    user_names.add(input())

for user in user_names:
    print(user)