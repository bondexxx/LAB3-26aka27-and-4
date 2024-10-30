import numpy as np


def column_operations(matrix):
    """
    Обчислює суму і добуток кожного стовпця в матриці.

    Parameters:
    matrix (np.array): Двовимірний масив numpy, що представляє матрицю.

    Returns:
    dict: Словник, що містить суми і добутки кожного стовпця.
    """
    sums = np.sum(matrix, axis=0)
    products = np.prod(matrix, axis=0)
    return {'sums': sums, 'products': products}


def matrix_sum(matrix1, matrix2):
    """
    Обчислює суму двох матриць.

    Parameters:
    matrix1 (np.array): Перша матриця.
    matrix2 (np.array): Друга матриця.

    Returns:
    np.array: Результуюча матриця після додавання.
    """
    return matrix1 + matrix2


def process_matrix(file_name):
    """
    Обробляє матрицю з вказаного файлу та виконує операції.

    Parameters:
    file_name (str): Ім'я файлу, що містить дані матриці.

    Returns:
    dict: Словник, що містить результати операцій з стовпцями та суму з випадковою матрицею.
    """
    try:
        matrix = np.loadtxt(file_name)
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при завантаженні файлу: {e}")
        return None

    col_ops = column_operations(matrix)

    random_matrix = np.random.rand(matrix.shape[0], matrix.shape[1])
    summed_matrix = matrix_sum(matrix, random_matrix)

    return {'column_operations': col_ops, 'summed_matrix': summed_matrix}


def task_matrix_4():
    """
    Введення даних (ім'я файлу), виклик функцій для обробки матриці, та виведення результатів.
    """
    file_name = input("Введіть ім'я файлу з даними матриці: ")
    results = process_matrix(file_name)

    if results is not None:
        print("Суми стовпців:", results['column_operations']['sums'])
        print("Добутки стовпців:", results['column_operations']['products'])
        print("Сума з випадковою матрицею:\n", results['summed_matrix'])


if __name__ == "__main__":
    task_matrix_4()
