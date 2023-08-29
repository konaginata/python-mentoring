def file_size(size_in_bytes):
    if not isinstance(size_in_bytes, int) or size_in_bytes < 0:
        raise ValueError("Input must be a non-negative integer")
    power = 2 ** 10
    count = 0
    while size_in_bytes >= power:
        size_in_bytes /= power
        count += 1
    labels = {0: 'B', 1: 'Kb', 2: 'Mb', 3: 'Gb'}
    return f"{size_in_bytes:.1f}{labels[count]}"


assert file_size(19) == '19.0B'
assert file_size(12345) == '12.1Kb'
assert file_size(1101947) == '1.1Mb'
assert file_size(572090) == '558.7Kb'
assert file_size(999999999999) == '931.3Gb'
