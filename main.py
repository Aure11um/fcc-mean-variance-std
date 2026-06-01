import mean_var_std

# 1. Тест с корректными данными (ровно 9 чисел)
print("--- Тест 1: Корректный список [0, 1, 2, 3, 4, 5, 6, 7, 8] ---")
try:
    result = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    
    # Красиво выводим получившийся словарь
    for key, value in result.items():
        print(f"'{key}': {value}")
        
except ValueError as e:
    print(f"Ошибка: {e}")

print("\n" + "="*50 + "\n")

# 2. Тест на ошибку (передаем только 3 числа вместо 9)
print("--- Тест 2: Проверка вызова ошибки (передаем [1, 2, 3]) ---")
try:
    mean_var_std.calculate([1, 2, 3])
except ValueError as e:
    print(f"Успешно поймали ожидаемую ошибку: {e}")
