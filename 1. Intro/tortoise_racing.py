def race(v1, v2, g):
    if v1 >= v2:
        return None

    time_hours = g / (v2 - v1)

    hours = int(time_hours)

    remaining_minutes = (time_hours - hours) * 60
    minutes = int(remaining_minutes)
    
    remaining_seconds = (remaining_minutes - minutes) * 60
    seconds = int(remaining_seconds)

    return [hours, minutes, seconds]

def test():
    result = race(720, 850, 70)
    if result:
        print(f"Результат: {result[0]}:{result[1]}:{result[2]}")
    else:
        print("Догнать невозможно")

    result = race(100, 200, 1000)
    if result:
        print(f"Результат: {result[0]}:{result[1]}:{result[2]}")

    result = race(500, 500, 100)
    if result:
        print(f"Результат: {result[0]}:{result[1]}:{result[2]}")
    else:
        print("Догнать невозможно")

if __name__ == "__main__":
    test()