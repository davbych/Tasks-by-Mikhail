user_input = input("Введите строку: ")
result = '-'.join(c.upper() + c.lower() * i for i, c in enumerate(user_input))
print(result)