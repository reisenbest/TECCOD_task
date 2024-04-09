'''
Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
и возвращает список всех простых чисел в заданном диапазоне.
'''


def prime_nums_from_min_to_max(min_val: int, max_val: int):
    try:
        if not isinstance(min_val, int) or not isinstance(max_val, int):
            raise TypeError("Аргументы должны быть целыми числами")

        if max_val < min_val:
            raise ValueError('Макисмальный элемент не может быть меньше минимального')

        if min_val <= 1:
            min_val = 2

        nums = range(min_val, max_val + 1)

        def is_prime(num):
            for el in range(2, int(num ** 0.5) + 1):
                if (num % el) == 0:
                    return False
            return True

        primes = list(filter(is_prime, nums))
        return primes

    except (TypeError, ValueError) as error:
        print(f"Ошибка: {error}")
        return error
