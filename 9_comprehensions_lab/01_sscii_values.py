# command = input().split(", ")
# ascii_dict = {}
# for ch in command:
#     ascii_dict[ch] = ord(ch)
# print(ascii_dict)


ascii_dict = {ch: ord(ch) for ch in input().split(", ")}
print(ascii_dict)