#  Напишите и запустите программу. которая выводит строку  "Hello world!"
print('Hello world!')

#  Напишите программу, которая на входе
#  получает имя пользователя, cохраняет его в переменную user_name и выводит строку  "Hello {user_name}!"

# user_name = input('Enter name -> ')
print(f'Hello {user_name}')


#  Напишите программу, которая на входе получает 2 числа,
#  производит с ними арифметическую операцию(на ваше усмотрение), и выводит “Результат = {результат}”.
num_1 = int(input('Enter number 1 -> '))
num_2 = int(input('Enter number 2 -> '))
print(f'Результат = {num_1 * num_2}')


#  Напишите программу, чтобы вывести:
def first_last(w, s):
    print(s * w)


def middle(w, l, s):
    n = (s + ' ' * (w - 2) + s + '\n') * l
    print(n, end='')


width = int(input('Ширина фигуры -> '))
lenght = int(input('Длинна фигуры -> '))
sumbol = input('Символ -> ')

first_last(width, sumbol)
middle(width, lenght, sumbol)
first_last(width, sumbol)
