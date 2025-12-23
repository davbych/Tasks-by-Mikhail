def generate_public_key(secret: int, g: int, p: int) -> int:
    result = g**secret % p
    return result

def generate_shared_secret(other_public: int, my_secret: int, p: int) -> int:
    result = other_public**my_secret % p
    return result


p = 23
g = 5

miha_secret = 6
miha_public = generate_public_key(miha_secret, g, p)
miha_shared = generate_shared_secret(miha_public, miha_secret, p)

dima_secret = 9
dima_public = generate_public_key(dima_secret, g, p)
dima_shared = generate_shared_secret(dima_public, dima_secret, p)

print("Открытый ключ Миши: ", miha_public) #8
print("Открытый ключ Димы: ", dima_public) #11

print("Секрет Миши: ", miha_shared) #9
print("Секрет Димы: ", dima_shared) #9

assert miha_shared == dima_shared, "Ошибка: общие ключи не совпадают!"