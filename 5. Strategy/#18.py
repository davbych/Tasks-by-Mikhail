def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros_count = len(lst) - len(non_zeros)
    return non_zeros + [0] * zeros_count

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))