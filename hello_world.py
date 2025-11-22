import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_square(number):
    try:
        num = float(number)
        return num * num
    except ValueError:
        return "Ошибка: введите число"

def main():
    print("=== Демонстрационное приложение ===")
    print(f"Текущее время: {get_current_time()}")
    
    # Базовая функциональность
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}!")
    
    # Новая функциональность v1.1.0
    number = input("Введите число для вычисления квадрата: ")
    result = calculate_square(number)
    print(f"Квадрат числа {number} равен: {result}")

if __name__ == "__main__":
    main()