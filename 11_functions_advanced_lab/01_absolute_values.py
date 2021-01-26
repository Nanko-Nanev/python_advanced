def absolut_values(number):
    result = []
    for n in number:
        result.append(abs(float(n)))
    return result


numbers_input = input().split()
abs_numbers = absolut_values(numbers_input)
print(abs_numbers)