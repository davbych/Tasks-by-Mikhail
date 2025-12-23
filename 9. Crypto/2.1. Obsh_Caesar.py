def obsh_caesar(text: str, shift: int, mode: str = "encrypt") -> str:

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.lower() in alphabet:
            pos = alphabet.find(char.lower())
            new_pos = (pos + shift) % len(alphabet)
            if char.isupper():
                result += alphabet[new_pos].upper()
            else:
                result += alphabet[new_pos]
        else:
            result += char

    return result

print(obsh_caesar("Hello", 55, 'encrypt'))
print(obsh_caesar("Khoor", 3, 'decrypt'))
print(obsh_caesar("XYZ", 5, 'encrypt'))
print(obsh_caesar("Hello, World!", 13, 'encrypt'))