def stock_availability(list_list, *args):
    from collections import deque

    if args[0] == "delivery":
        list_list.append(', '.join(args[1:]))

    elif args[0] == "sell":
        if len(args) >= 2:
            for el in args:
                if str(el).isdigit():
                    for i in range(int(args[1])):
                        list_list.remove(list_list[0])
            else:
                for el in args:
                    if el in list_list:
                        list_list.remove(el)
        elif len(args) == 1:
            list_list.remove(list_list[0])

    return list_list

