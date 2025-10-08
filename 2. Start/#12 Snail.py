def snail(array):
    result = []
    while array:
        result += array.pop(0)
        for row in array:
            if row:
                result.append(row.pop())
        if array:
            result += array.pop()[::-1]
        for row in array[::-1]:
            if row:
                result.append(row.pop(0))
    return result

array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
array2 = [[1, 2, 3, 4],
          [12, 13, 14, 5],
          [11, 16, 15, 6],
          [10, 9, 8, 7]]
print(snail(array1))
print(snail(array2))