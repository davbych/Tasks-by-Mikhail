def remove_elements(a, b):
    b_set = set(b)
    result = [element for element in a if element not in b_set]
    return result


def get_numbers(prompt):
    n = int(input("Сколько элементов будет в списке? "))
    numbers = []
    for i in range(n):
        while True:
            try:
                num = int(input(f"{prompt} элемент {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Ошибка! Введите целое число.")
    return numbers

if __name__ == "__main__":
    print("Ввод списка a:")
    list_a = get_numbers("Введите")

    print("\nВвод списка b:")
    list_b = get_numbers("Введите")

    result = remove_elements(list_a, list_b)
    print("\nРезультат:", result)