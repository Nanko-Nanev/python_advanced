# command = input().split(", ")
# result = []
# for word in command:
#     result.append(f"{word} -> {len(word)}")
# print(*result, sep=", ")

print(*[f"{word} -> {len(word)}" for word in input().split(", ")], sep=", ")

