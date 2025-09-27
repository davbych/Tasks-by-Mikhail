def tetration_iterative(n, x):
    result = x
    for _ in range(n - 1):
        result = x ** result
    return result

print(tetration_iterative(2, 5))
print(tetration_iterative(2, 2))
print(tetration_iterative(3, 2))
print(tetration_iterative(4, 2))
