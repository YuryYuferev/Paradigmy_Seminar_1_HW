# Задача- 1: У вас есть массив целых чисел, в котором каждое число, кроме одного, повторяется дважды.
# Вам нужно найти это одиночное число.
# def find_single_number(nums):
#     # Инициализируем переменную, которая будет хранить результат
#     result = 0
#
#     # Проходим по всем элементам массива
#     for num in nums:
#         # Каждое число XOR-им с результатом
#         # Поскольку XOR дважды примененный к одному и тому же числу даёт 0,
#         # то результатом будет одиночное число
#         result ^= num
#
#     # Возвращаем найденное одиночное число
#     return result
#
# array = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
# print(find_single_number(array))



# Задача-2: У вас есть массив, содержащий числа от 1 до N, где N - длина массива.
# Одно из чисел в массиве повторяется дважды, а одно число пропущено.
# Найдите повторяющееся число и пропущенное число.

def find_duplicate_and_missing(arr):
    n = len(arr)  # Длина массива
    sum_actual = sum(arr)  # Сумма чисел в массиве

    # Ожидаемая сумма чисел от 1 до N
    sum_expected = (n * (n + 1)) // 2

    # Найдем разницу между реальной суммой и ожидаемой суммой
    diff = sum_actual - sum_expected

    duplicate = None
    missing = None

    # Пройдемся по каждому элементу массива
    for num in arr:
        # Если элемент уже встречался, значит это повторяющееся число
        if arr[abs(num) - 1] < 0:
            duplicate = abs(num)
        else:
            arr[abs(num) - 1] *= -1  # Изменим знак элемента, чтобы пометить его как встреченный

    # Пройдемся по массиву еще раз, чтобы найти пропущенное число
    for i in range(len(arr)):
        # Если элемент положительный, значит он ни разу не встречался и это пропущенное число
        if arr[i] > 0:
            missing = i + 1
            break

    return duplicate, missing

arr = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9]
duplicate, missing = find_duplicate_and_missing(arr)

print("Повторяющееся число:", duplicate)
print("Пропущенное число:", missing)

