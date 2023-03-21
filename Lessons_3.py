# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
print(*my_list[2], sep='\n')


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

print(sum(filter(lambda y: isinstance(y, int), list_1)))
for i in list_1:
    if 'a' in str(i):
        print(i)

# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

tupl = tuple(['cat', 'dog', 'horse', 'cow'])
print(type(tupl))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом.
#      Если состав одинаковый, print("Equal')

family_1 = input('Enter family list using "," as spliter -> ')
family_2 = input('Enter family list using "," as spliter -> ')

family_1 = family_1.split(',') if family_1 != '' else []
family_2 = family_2.split(',') if family_2 != '' else []

if len(family_1) > len(family_2):
    print(*family_1, sep=',')
elif len(family_1) < len(family_2):
    print(*family_2, sep=',')
else:
    print('Equal')


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
film = {
    'title': 'The Curious Case of Benjamin Button',
    'director': 'David Fincher',
    'year': '2008',
    'budget': '$150–167 million',
    'main_actor': 'Brad Pitt',
    'slogan': "Life isn't measured in minutes, but in moments"
        }

print(film)
print(film.values())
print(film.items())



# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))



# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

lst2 = [1, 2, 3, 4, 5, 3, 2, 1]
count = 0
while count < len(lst2):
    if lst2[count] in lst2[count+1:]:
        del lst2[lst2.index(lst2[count])]
        continue
    count += 1
print(lst2)

# or
lst2_set = set(lst2)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))