start = int(input())
end = int(input())
# range_d = (2, 10)
result = []
#
# for i in range(start, end + 1):
#     if any(i % x == 0 for x in range(2, 11)):
#         result.append(i)
# print(result)
result.append([i for i in range(start, end + 1) if any(i % x == 0 for x in range(2, 11))])

print(*result)