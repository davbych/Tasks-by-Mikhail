def binary_gcd(x, y):

    if x == 0 and y == 0:
        return 0

    a, b = abs(x), abs(y)

    while b:
        a, b = b, a % b

    return bin(a).count('1')

print(binary_gcd(300, 45))
print(binary_gcd(666666, 333111))
print(binary_gcd(545034, 5))
print(binary_gcd(0, 0))
print(binary_gcd(0, 76899299))
print(binary_gcd(-124, -16))
