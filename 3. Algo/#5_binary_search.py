def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(binary_search([1,2,3,4,5,6,7], 4))
print(binary_search([1,2,3,4,5,6,7], 6))
print(binary_search([1,2,3,4,5,6,7], 1))
print(binary_search([1,2,3,4,5,6,7], 8))
print(binary_search([], 1))