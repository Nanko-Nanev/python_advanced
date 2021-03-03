from collections import deque


def stock_availability(list_list, cmd, *args):

    boxes_list = deque(list_list)
    if cmd == "delivery":
        for item in args:
            boxes_list.append(item)
        return list(boxes_list)
    elif cmd == "sell":
        if not args:
            boxes_list.popleft()
            return list(boxes_list)
        else:
            for item in args:
                if str(item).isdigit():
                    for i in range(item):
                        boxes_list.popleft()
                    return list(boxes_list)
                else:
                    for itm in args:
                        while itm in args:
                            boxes_list.remove(itm)
                        return list(args)



5
