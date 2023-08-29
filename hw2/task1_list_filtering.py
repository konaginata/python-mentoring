def filter_list_loop(original_list):
    filtered_list = []
    for item in original_list:
        if isinstance(item, int):
            filtered_list.append(item)
    return filtered_list


def filter_list_comprehension(original_list):
    return [item for item in original_list if isinstance(item, int)]


def filter_list_lambda(original_list):
    return list(filter(lambda x: isinstance(x, int), original_list))


list1 = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
list2 = [1, 2, 'a', 'b']
list3 = [1, 'a', 'b', 0, 15]
list4 = [1, 2, 'asf', '1', '123', 123]

assert filter_list_loop(list1) == filter_list_comprehension(list1) == filter_list_lambda(list1) == [1, 2, 4, 10, 33]
assert filter_list_loop(list2) == filter_list_comprehension(list2) == filter_list_lambda(list2) == [1, 2]
assert filter_list_loop(list3) == filter_list_comprehension(list3) == filter_list_lambda(list3) == [1, 0, 15]
assert filter_list_loop(list4) == filter_list_comprehension(list4) == filter_list_lambda(list4) == [1, 2, 123]
