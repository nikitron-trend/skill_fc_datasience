"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
# импортируем библиотеку
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    s = 1
    e = 101

    while True:
        count += 1
        predict_number = np.random.randint(s, e)  # предполагаемое число
        if predict_number > number: # если происходит 'перелет' или 'недолет' предсказанного числа то меняем диапазон
            e = predict_number
        elif predict_number < number:
            s = predict_number
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

