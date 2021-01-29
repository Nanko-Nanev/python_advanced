def sort_numbers_ascending(numbers):
    return sorted(numbers)


list_of_numbers = [int(el) for el in input().split()]
print(sort_numbers_ascending(list_of_numbers))