def size_to_number(size):
    sizes = ['s', 'm', 'l']
    if len(size) < 1 or size[-1] not in sizes:
        return None
    base_size = size[-1]
    added_x = size[:-1]
    if base_size == 'm' and len(added_x) > 0:
        return None
    if any(char not in 'xsml' for char in size):
        return None
    base_size_count = 0
    for s in sizes:
        base_size_count += size.count(s)
        if base_size_count > 1:
            return None
    count_x = len(added_x)
    if base_size == 's':
        final_size = 36 - 2 * count_x
    elif base_size == 'm':
        final_size = 38
    elif base_size == 'l':
        final_size = 40 + 2 * count_x
    else:
        return None
    return final_size



print(size_to_number('xxxxxxxxxxxxl'))