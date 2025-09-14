from datetime import datetime
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
current_year = datetime.now().year
year_100 = current_year + (100 - age)
print(f"Здравствуйте, {name}!")
print(f"При текущей скорости старения вы достигнете возраста 100 лет в {year_100} году.")