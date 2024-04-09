'''
4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.

'''


def sort_strings_by_length(strings):
    '''
    строки сортируются исключительно по количеству симвлов, если одинаковая длина - влияет индекс элемента в списке
    '''

    try:
        strings = strings.split()

        if not strings:
            raise ValueError("Вы ничего не ввели")

        strings.sort(key=len)
        print("Список строк, отсортированный по возрастанию длины:")
        print(strings)

        strings.sort(key=len, reverse=True)
        print("Список строк, отсортированный по убыванию длины:")
        print(strings)

    except ValueError as e:
        print(f"Ошибка: {e}")


user_input = input("Введите строки через пробел: ")
sort_strings_by_length(user_input)
