def calculate_triangular_sum(limit, diff):
    num_terms = limit // diff
    return diff * (num_terms * (num_terms + 1) // 2)


def sum_multiples_of_3_or_5(limit):
    upper_limit = limit - 1
    sum_multiples_of_3 = calculate_triangular_sum(upper_limit, 3)
    sum_multiples_of_5 = calculate_triangular_sum(upper_limit, 5)
    sum_multiples_of_15 = calculate_triangular_sum(upper_limit, 15)
    return sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_15


print(sum_multiples_of_3_or_5(100000000))


# calculation check - slow:
def checking_calculation(limit):
    total = 0
    for num in range(1, limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total


assert sum_multiples_of_3_or_5(100000000) == checking_calculation(100000000)
