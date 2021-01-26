def rounding(number):
    result = []
    for el in number:
        result.append(round(float(el)))
    return result


numbers = input().split()
print(rounding(numbers))