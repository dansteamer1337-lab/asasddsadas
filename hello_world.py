import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_square(number):
    try:
        num = float(number)
        return num * num
    except ValueError:
        return "Ошибка: введите число"

def validate_name(name):
    if not name or not name.strip():
        return False
    return True

def main():
    print("=== Демонстрационное приложение ===")
    print(f"Текущее время: {get_current_time()}")
    print()
    
    # Базовая функциональность с валидацией
    while True:
        name = input("Введите ваше имя: ").strip()
        if validate_name(name):
            break
        print("Ошибка: имя не может быть пустым. Попробуйте снова.")
    
    print(f"Привет, {name}!")
    
    # Новая функциональность v1.1.0
    while True:
        number = input("Введите число для вычисления квадрата: ").strip()
        result = calculate_square(number)
        if isinstance(result, (int, float)):
            print(f"Квадрат числа {number} равен: {result}")
            break
        else:
            print(result)

if __name__ == "__main__":
    main()