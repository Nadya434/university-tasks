def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def main():
    print("=== Простой калькулятор ===")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    choice = input("Выберите опцию (1-4): ")
    
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    
    if choice == '1':
        print(f"Результат: {add(a, b)}")
    elif choice == '2':
        print(f"Результат: {subtract(a, b)}")
    elif choice == '3':
        print(f"Результат: {multiply(a, b)}")
    elif choice == '4':
        print(f"Результат: {divide(a, b)}")
    else:
        print("Неверный выбор!")

if __name__ == "__main__":
    main()