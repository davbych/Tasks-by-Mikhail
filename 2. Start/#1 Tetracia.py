def tetration(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x ** tetration(n - 1, x)

print(tetration(1, 2))
print(tetration(3, 2))
print(tetration(2, 5))
print(tetration(4, 2))