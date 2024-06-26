"""
Ця програма переводить число секунд у формат часу у читабельному вигляді.
Користувач вводить число від 0 до 8639999, яке представляє кількість секунд.
Програма розраховує та виводить кількість днів, годин, хвилин та секунд у форматованому вигляді.
Слово "день" підбирається на основі кількості днів, а години, хвилини та секунди заповнюються
провідними нулями при одноцифрових значеннях.
"""

# Отримуємо кількість секунд від користувача
total_seconds = int(input("Введіть кількість секунд (від 0 до 8639999): "))

# Перевіряємо, чи введене число в допустимому діапазоні
if 0 <= total_seconds < 8640000:
    # Розраховуємо кількість днів, годин, хвилин та секунд
    days, seconds_left = divmod(total_seconds, 86400)
    hours, seconds_left = divmod(seconds_left, 3600)
    minutes, seconds = divmod(seconds_left, 60)

    # Визначаємо правильне закінчення слова "день" в залежності від кількості днів
    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "дні"
    else:
        day_word = "днів"

    # Форматуємо вивід, доповнюючи числа провідними нулями
    print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print("Введене число повинно бути від 0 до 8639999.")
