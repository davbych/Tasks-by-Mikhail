rng = int(input('Введите число: '))
useful = []
for i in range(rng):
    if i % 3 == 0 or i % 5 == 0:
        useful.append(i)
print(sum(useful))