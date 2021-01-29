def negative_vs_positive(numbers):
    # sum_negative = sum([num for num in numbers if num < 0])
    # sum_positive = sum([num for num in numbers if num > 0])
    sum_negative = sum(filter(lambda x: x < 0, numbers))
    sum_positive = sum(filter(lambda x: x > 0, numbers))
    return sum_negative, sum_positive


list_of_numbers = [int(el) for el in input().split()]
# list_of_numbers = map(int, input().split())
result = negative_vs_positive(list_of_numbers)


print(result[0])
print(result[1])

if abs(result[0]) > result[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")