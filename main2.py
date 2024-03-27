def calculate_alphabet_strength(password: str):
    lower_case = False
    upper_case = False
    digits = False
    symbols = False

    # Определение символов, содержащихся в пароле
    for char in password:
        if char.islower():
            lower_case = True
        elif char.isupper():
            upper_case = True
        elif char.isdigit():
            digits = True
        else:
            symbols = True

    # Определение мощности алфавита
    alphabet_strength = 0
    if lower_case:
        alphabet_strength += 26
    if upper_case:
        alphabet_strength += 26
    if digits:
        alphabet_strength += 10
    if symbols:
        alphabet_strength += 33

    return alphabet_strength


def calculate_search_time(password: str, alphabet_strength: int, speed: float, attempts_threshold: int,
                          delay_seconds: int) -> tuple:
    possible_passwords_count = alphabet_strength ** len(password)
    # Время ожидания после ввода неправильных паролей
    try_count = possible_passwords_count // attempts_threshold
    if possible_passwords_count % attempts_threshold == 0:
        try_count -= 1
    delay_time = try_count * delay_seconds
    # Общее время
    time = possible_passwords_count / speed + delay_time

    minute = 60
    hour = 60 * minute
    day = 24 * hour
    month = 30 * day
    year = 365 * day

    # Конечное время
    year_result = time // year
    month_result = (time - year * year_result) // month
    day_result = (time - year * year_result - month_result * month) // day
    hour_result = (time - year * year_result - month_result * month - day_result * day) // hour
    minute_result = (time - year * year_result - month_result * month - day_result * day - hour * hour_result) // minute
    second_result = (time - year * year_result - month_result * month - day_result * day - hour * hour_result -
                     minute_result * minute)

    return year_result, month_result, day_result, hour_result, minute_result, second_result, possible_passwords_count


def main():
    password = input("Введите пароль: ")
    speed_per_second = float(input("Скорость перебора паролей в секунду: "))
    attempts_threshold = int(input("Количество неправильных попыток: "))
    delay_seconds = int(input("Пауза: "))

    alphabet_strength = calculate_alphabet_strength(password)
    time = calculate_search_time(password, alphabet_strength, speed_per_second, attempts_threshold, delay_seconds)

    print("Мощность алфавита: {0}".format(alphabet_strength))
    print("Количество всевозможных паролей: {0}".format(time[6]))
    print("Полное время перебора: ")
    print("{0} лет {1} месяцев {2} дней {3} часов {4} минут {5} секунд".format(time[0], time[1], time[2], time[3],
                                                                               time[4], time[5]))


if __name__ == "__main__":
    main()
