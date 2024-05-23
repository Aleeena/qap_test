# # Двоичный поиск
#
# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 98))


def binary_search(array, element):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = left + right
        number = array[middle]
        if array[middle-1] < number <= array[middle-1]:
            return middle-1
        elif number > element:
            right = middle - 1
        else:
            left = middle + 1
    return None


new_list = [1, 3, 5, 6, 8, 9]
print(binary_search(new_list, 8))
