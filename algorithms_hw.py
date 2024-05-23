list_numbers = list(map(int, input("Введите последовательность чисел через пробел: ").split()))


def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle - 1] < element < array[middle]:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


sorted_nums = sort(list_numbers)

try:
    control_num = int(input("Введите любое число: "))
    if control_num > sorted_nums[-1] or control_num < sorted_nums[0]:
        raise ValueError("Повторите попытку")
except ValueError as e:
    print('Число не входит в диапазон (от ' + str(sorted_nums[0]) + ' до ' + str(sorted_nums[-1]) + ')')
else:
    print(sorted_nums)
    print("Индекс элемента, который меньше введенного числа: ",
          binary_search(sorted_nums, control_num, 0, (len(sorted_nums)) - 1))
