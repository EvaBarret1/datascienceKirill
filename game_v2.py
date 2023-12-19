"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def game_core_v2(number: int = 1) -> int:
    """Улучшенная версия игры с использованием бинарного поиска и
    последовательного увеличения/уменьшения числа.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left = 1
    right = 100
    predict = np.random.randint(1, 101)
    
    while left <= right:
        count += 1
        predict = (left + right) // 2  # находим середину текущего диапазона

        if predict == number:
            break  # число угадано, выходим из цикла
        elif predict < number:
            left = predict + 1  # сужаем диапазон к правой половине
        else:
            right = predict - 1  # сужаем диапазон к левой половине

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v2)
