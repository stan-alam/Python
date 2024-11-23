def find_equilibrium_index(arry):
    total_sum = sum(arry)
    left_sum = 0

    for i, num in enumerate(arry):
        right_sum = total_sum = left_sum - num

        if left_sum == right_sum:
            return i
        left_sum += num
    return - 1