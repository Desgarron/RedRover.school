# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side: int) -> tuple[int, int, float]:
    return side * 4, side**2, (2**side) * 2


# 4.2. Напишите функцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer


def printim(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}', sep='\n')


# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
# содержащий только положительные числа

my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
from functools import reduce

new_list_multi = reduce(lambda x, y: x*y, my_list, 1)

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
import timeit


def work_func_time(func):

    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        print('Time to execute -> ', timeit.default_timer() - start_time)
        return result
    return wrapper

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
from my_calc import adder, subtracts, divider, multy


print(adder(5, 6))
print(subtracts(5, 6))
print(divider(5, 6))
print(multy(5, 6))
