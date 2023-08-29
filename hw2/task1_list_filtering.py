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


tests = [
    ([1, 2, '3', 4, None, 10, 33, 'Python', -37.5], [1, 2, 4, 10, 33]),
    ([1, 2, 'a', 'b'], [1, 2]),
    ([1, 'a', 'b', 0, 15], [1, 0, 15]),
    ([1, 2, 'asf', '1', '123', 123], [1, 2, 123])
]
for initial, expected in tests:
    assert filter_list_loop(initial) == expected
    assert filter_list_comprehension(initial) == expected
    assert filter_list_lambda(initial) == expected
