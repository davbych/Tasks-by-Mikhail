def linear_search(arr, target):
    if target not in arr:
        return -1
    return arr.index(target)


print(linear_search([5, 3, 7, 1, 4], 1))
print(linear_search([10, 20, 30, 40], 30))
print(linear_search([1, 2, 3, 4], 5))
print(linear_search([1], 1))
print(linear_search([], 1))