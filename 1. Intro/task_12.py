chislo, varik = map(int, input("<Число битов>, <1 - байты/2 - килобайты> \n ").split(","))
if varik == 1:
    print(chislo/8)
elif varik == 2:
    print((chislo/8)/1024)
else:
    print("Неверный выбор")