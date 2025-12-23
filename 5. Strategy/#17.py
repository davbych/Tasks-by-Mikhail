str1 = input("1: ").strip()
str2 = input("2: ").strip()

if str1.lower() < str2.lower():
    print(-1)
elif str1.lower() > str2.lower():
    print(1)
else:
    print(0)

# Пример использования:
# Ввод:
# aaaa
# aaaA
# Вывод:
# 0