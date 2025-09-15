kol = int(input("Людей: "))
num = input("Занятые места: ").split()
b = [0]*(kol+1)
for i in range(1, kol+1):
    seat = int(num[i-1])
    b[seat] = i
print(b[1:])