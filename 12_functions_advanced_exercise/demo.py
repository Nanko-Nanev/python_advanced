numbers = [1, 3, 5, 34, 7, 9, 12, 11, 13, 10]

sum_of_numbers = list(map(lambda num: num % 2 == 0, numbers))

print(sum_of_numbers)