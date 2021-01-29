def odd_or_even_sum_by_length(odd_even, numbers):
    sum_of_numbers = 0
    if odd_even == "Odd":
        sum_of_numbers = list(filter(lambda el: el % 2 !=0, numbers))
    elif odd_even == "Even":
        sum_of_numbers = [el for el in numbers if el % 2 ==0]
    # return list(sum_of_numbers)
    return sum(sum_of_numbers) * len(numbers)


command = input()
list_of_numbers = [int(el) for el in input().split()]
print(odd_or_even_sum_by_length(command, list_of_numbers))