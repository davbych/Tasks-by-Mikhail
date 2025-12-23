import string

def caesar_cipher(text, shift, decrypt=False):
    # alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    if decrypt:
        shift = -shift

    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            pos = alphabet.find(char.lower())
            # Вычисляем новую позицию с учётом сдвига и «закольцовывания»
            new_pos = (pos + shift) % len(alphabet)
            result += alphabet[new_pos].upper() if is_upper else alphabet[new_pos]
        else:
            result += char

    return result


def main():
    print("Шифр Цезаря (английский алфавит)")
    # print("Шифр Цезаря (русский алфавит)")
    while True:
        print("\n1. Зашифровать")
        print("2. Расшифровать")
        print("3. Выход")
        choice = input("Выберите действие (1-3): ")

        if choice == '3':
            break
        elif choice in ('1', '2'):
            text = input("Введите текст: ")
            shift = int(input("Введите сдвиг (целое число): "))

            if choice == '1':
                result = caesar_cipher(text, shift)
                print("Зашифрованный текст:", result, shift)
            else:
                result = caesar_cipher(text, shift, decrypt=True)
                print("Расшифрованный текст:", result)
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":

    main()
