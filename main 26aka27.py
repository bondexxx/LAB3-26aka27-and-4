def IsPower5(K):
    """
    Перевіряє, чи є ціле число K ступенем числа 5.

    Parameters:
    K (int): Ціле число для перевірки.

    Returns:
    bool: True, якщо K є ступенем числа 5, False в іншому випадку.
    """
    if K <= 0 or K >= 3000:
        return False
    while K % 5 == 0:
        K //= 5
    return K == 1


def check_powers_of_5(numbers):
    """
    Перевіряє список цілих чисел, чи є вони ступенями числа 5.

    Parameters:
    numbers (list): Список цілих чисел для перевірки.

    Returns:
    list: Список булевих значень, що вказують, чи є відповідне число ступенем числа 5.
    """
    return [IsPower5(num) for num in numbers]


def task26():
    """
    Введення даних, виклик функції для перевірки ступенів числа 5, та виведення результатів.
    """
    in_data = []
    for i in range(10):
        temp = int(input("Введіть число: "))
        in_data.append(temp)
    out_data = check_powers_of_5(in_data)
    print("Числа, що є ступенями числа 5: ", out_data)


if __name__ == "__main__":
    task26()
