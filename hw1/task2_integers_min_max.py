numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
print("All values:", numbers)

integers = []
for val in numbers:
    try:
        integers.append(int(val))
    except (TypeError, ValueError):
        pass
print("Integer values:", integers)

print('Min value is', min(integers))
print('Max value is', max(integers))
