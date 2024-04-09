'''
Написать функцию, которая принимает на вход список целых чисел и возвращает новый список,
содержащий только уникальные элементы из исходного списка.
'''


def unique_els_from_list(start_array: list):
    try:
        if not isinstance(start_array, list):
            raise TypeError("Аргумент должен быть списком")

        if not all(isinstance(x, int) for x in start_array):
            raise ValueError("Список должен содержать только целые числа")

        if len(start_array) == 0:
            raise IndexError('Список пустой')

        # про то, что числа в конечном списке должны сохранить свой порядок ничего сказано не было
        # если это нужно можно применить сортировку к результирующему списку
        # или создавать отдельный список и туда складывать значения через цикл которые не повторялись
        return list(set(start_array))

    except (TypeError, ValueError, IndexError) as error:
        print(f"Ошибка: {error}")
        return error
