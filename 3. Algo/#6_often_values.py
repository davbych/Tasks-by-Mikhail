def most_frequent_value_count(n, q, array, queries):
    result = []
    for i, j in queries:
        left = i - 1
        right = j - 1
        if left > right or left < 0 or right >= n:
            result.append(0)
            continue
        max_count = 0
        current_count = 1
        for idx in range(left + 1, right + 1):
            if array[idx] == array[idx - 1]:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 1
        max_count = max(max_count, current_count)
        result.append(max_count)
    return result


def test_most_frequent_value_count():
    # Тест 1
    n1, q1 = 10, 3
    array1 = [-1, -1, 1, 1, 1, 1, 3, 10, 10, 10]
    queries1 = [(2, 3), (1, 10), (5, 10)]
    expected1 = [1, 4, 3]
    assert most_frequent_value_count(n1, q1, array1, queries1) == expected1

    # Тест 2
    n2, q2 = 5, 2
    array2 = [1, 1, 2, 2, 2]
    queries2 = [(1, 5), (2, 4)]
    expected2 = [3, 2]
    assert most_frequent_value_count(n2, q2, array2, queries2) == expected2

    # Тест 3
    n3, q3 = 6, 3
    array3 = [3, 3, 4, 4, 4, 5]
    queries3 = [(1, 2), (1, 6), (3, 6)]
    expected3 = [2, 3, 3]
    assert most_frequent_value_count(n3, q3, array3, queries3) == expected3

    # Тест 4
    n4, q4 = 1, 1
    array4 = [7]
    queries4 = [(1, 1)]
    expected4 = [1]
    assert most_frequent_value_count(n4, q4, array4, queries4) == expected4

    # Тест 5
    n5, q5 = 7, 3
    array5 = [1, 2, 2, 3, 3, 3, 4]
    queries5 = [(1, 7), (2, 5), (3, 7)]
    expected5 = [3, 2, 3]
    assert most_frequent_value_count(n5, q5, array5, queries5) == expected5

    # Тест 6: Пустой массив
    n6, q6 = 0, 0
    array6 = []
    queries6 = []
    expected6 = []
    assert most_frequent_value_count(n6, q6, array6, queries6) == expected6

    print("OK!")
test_most_frequent_value_count()