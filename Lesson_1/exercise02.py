# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input("Введите время в секундах: "))

hours = time_in_seconds // 3600
print("часов: ", hours)

minutes = (time_in_seconds - (hours * 3600)) // 60
print("минут: ", minutes)

seconds = time_in_seconds - (hours * 3600 + minutes * 60)
print("секунд: ", seconds)

print(f"Время в формате чч:мм:сс   {hours}:{minutes}:{seconds}")
