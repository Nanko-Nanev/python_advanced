command_line = input()
unique_chars = {}

for ch in command_line:
    if ch not in unique_chars:
        unique_chars[ch] = 0
    unique_chars[ch] += 1

# for k, v in unique_chars.items():
#     print(f"{k}: {v} time/s")
for k, v in sorted(unique_chars.items()):
    print(f"{k}: {v} time/s")