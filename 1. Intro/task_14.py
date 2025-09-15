days = int(input("Дни в месяце: "))
day = 1
for i in range(1, days):
    print("   ", end="")
i = days
while day <= days:
    if day <= 10:
        print(f" {day}", end="")
    else:
        print(f"{day}", end="")
    if i % 7 == 0 or day == days:
        print()
    else:
        print(" ", end="")
    day+=1
    i+=1