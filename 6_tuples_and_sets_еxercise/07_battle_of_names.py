# from collections import deque
#
# n = int(input())
# ascii_sum = 0
# odd_numbers = deque([])
# even_numbers = deque([])
#
# for i in range(n):
#     name = input()
#     for ch in name:
#         ascii_sum += ord(ch)
#     name_value = ascii_sum // len(name)
#     if name_value % 2 == 0:
#         even_numbers.append(name_value)
#     else:
#         odd_numbers.append(name_value)
#     ascii_sum = 0
#
# sum_odd_numbers = sum(odd_numbers)
# sum_even_numbers = sum(even_numbers)
#
# if sum_even_numbers == sum_odd_numbers:
#     pass
# elif sum_odd_numbers > sum_even_numbers:
#     sum_even_numbers.symm