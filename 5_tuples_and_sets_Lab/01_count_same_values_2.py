items_to_count = input().split()
counted_items = {}

for el in items_to_count:
    if el not in counted_items:
        counted_items[el] = 0
    counted_items[el] += 1

for key, value in counted_items.items():
    print(f"{float(key):.1f} - {value} times")