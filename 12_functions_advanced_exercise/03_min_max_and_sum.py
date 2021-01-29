def min_max_sum(numbers):
    min_numb = min(numbers)
    max_numb = max(numbers)
    sum_numb = sum(numbers)
    return min_numb, max_numb, sum_numb


# list_of_numbers = [int(el) for el in input().split()]
list_of_numbers = list(map(int, input().split()))
result = min_max_sum(list_of_numbers)
print(
    f"The minimum number is {result[0]}\n" 
    f"The maximum number is {result[1]}\n"
    f"The sum number is: {result[2]}"
)

