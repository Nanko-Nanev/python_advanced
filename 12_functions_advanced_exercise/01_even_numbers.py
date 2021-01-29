def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


# list_of_numbers = [int(el) for el in input().split()]
list_of_numbers = map(int, input().split())
print(even_numbers(list_of_numbers))