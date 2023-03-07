# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

hp = int(input("Enter hp for your pers --> "))
print(hp > 0)


# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

number = int(input('Enter the number -->'))
print('Четное' if number % 2 == 0 else 'Нечетное')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)

year = int(input('Enter the year -->'))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Год високосный")
else:
    print('Год невисокосный')


# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

text = input()
times = int(input())

print((text + '\n') * times, end='')

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator} {num2} = {result}

num1 = int(input('Enter number 1 --> '))
num2 = int(input('Enter number 2 --> '))
operrator = input('Enter operator [+, -, *, /] --> ')

if operrator == "+":
    print(f"{num1} {operrator} {num2} = {num1+num2}")
elif operrator == "-":
    print(f"{num1} {operrator} {num2} = {num1 - num2}")
elif operrator == "*":
    print(f"{num1} {operrator} {num2} = {num1 * num2}")
elif operrator == '/':
    if num2 == 0:
        print('Error divide on zero')
    else:
        print(f"{num1} {operrator} {num2} = {num1 / num2}")
