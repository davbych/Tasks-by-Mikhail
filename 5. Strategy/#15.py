def fill(arr, method):
    if not arr:
        return []

    n = len(arr)
    result = arr.copy()

    if method == -1:
        for i in range(n - 2, -1, -1):
            if result[i] is None and result[i + 1] is not None:
                result[i] = result[i + 1]

    elif method == 1:
        for i in range(1, n):
            if result[i] is None and result[i - 1] is not None:
                result[i] = result[i - 1]

    elif method == 0:
        result = arr.copy()
        for i in range(n):
            if result[i] is None:
                left_val, left_dist = None, float('inf')
                right_val, right_dist = None, float('inf')

                for j in range(i - 1, -1, -1):
                    if result[j] is not None:
                        left_val = result[j]
                        left_dist = i - j
                        break

                for j in range(i + 1, n):
                    if result[j] is not None:
                        right_val = result[j]
                        right_dist = j - i
                        break

                if left_dist < right_dist:
                    result[i] = left_val
                elif right_dist < left_dist:
                    result[i] = right_val
                else:
                    if left_val is not None and right_val is not None:
                        result[i] = min(left_val, right_val)
                    elif left_val is not None:
                        result[i] = left_val
                    elif right_val is not None:
                        result[i] = right_val

        return result
    return result


arr = [None, 1, None, None, None, 2, None]

print(fill(arr, -1))
print(fill(arr,  0))
print(fill(arr,  1))
print(fill([], 0))
print(fill([None], 0))
