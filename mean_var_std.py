import numpy as np

def calculate(list):
    # Проверяем, что в списке ровно 9 элементов
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Превращаем список в матрицу 3x3
    matrix = np.array(list).reshape(3, 3)
    
    # Считаем все необходимые метрики
    # В NumPy: axis=0 — это вычисления по вертикали (для колонок), 
    # а axis=1 — по горизонтали (для строк).
    # Метод .tolist() обязателен, так как freeCodeCamp требует нативные списки Python.
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum()
        ]
    }

    return calculations
