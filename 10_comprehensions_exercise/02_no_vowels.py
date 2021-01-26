vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union(x.upper() for x in vowels)
command = input()
# result = ""

# for ch in command:
#     if ch not in vowels:
#         result += ch
#
# print(result)
result = [ch for ch in command if ch not in vowels]
print(*result, sep="")