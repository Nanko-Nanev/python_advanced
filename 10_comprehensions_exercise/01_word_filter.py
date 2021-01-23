# command = input().split()
# for word in command:
#     if len(word) % 2 == 0:
#         print(word)


# print(*[word for word in input().split() if len(word) % 2 == 0])
words = [word for word in input().split() if len(word) % 2 == 0]
for word in words:
    print(word)