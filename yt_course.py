x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))


def summ(x, y):
    return x + y


def subt(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def power(x, y):
    return x ** y


operations = ['1-сложение', '2-вычетание', '3-умножение', '4-деление', '5-степень']

calculation = [
    summ(x, y),
    subt(x, y),
    mult(x, y),
    div(x, y),
    power(x, y)
]


print('\nВыберите операцию:')

for operation in operations:
    print(operation)


choose = int(input('\nВаш выбор: ')) - 1


if len(calculation) > choose:
    print('Результат:', calculation[choose])
else:
    print('Введите корректный номер операции!')







