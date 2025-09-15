def evenFibSum(limit):
    a, b = 1, 2
    even_sum = 0
    while b <= limit:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    return even_sum


def test():
    test_cases = [
        (13, 10),
        (34, 44),
        (100, 44),
        (200, 188),
        (10000, 3382),
        (4000000, 4613732)
    ]
    for i, (limit, expected) in enumerate(test_cases, 1):
        try:
            result = evenFibSum(limit)
            if result != expected:
                print(f"Тест {i} не пройден. Ожидалось: {expected}, получено: {result}")
                return False
        except Exception as e:
            print(f"Ошибка в тесте {i}: {str(e)}")
            return False
    print("Все тесты пройдены!")
    return True


if __name__ == "__main__":
    test()