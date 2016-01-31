# -*- coding: utf-8 -*-



print('Задание 1: реверс строки\n')
'''
УСЛОВИЕ:
Преобразовать строку "ecnalubma" в ее зеркальное отражение (реверсировать).
Сделать это четырьмя разными способами.
ВХОД: строка
ВЫХОД: реверсированная строка
Пример:
a = "ambulance"
...
print result
> "ecnalubma"
'''

a = 'ambulance'

print('способ 1:')

result = ''
for i in reversed(a):
	result += i
print(result)

print('способ 2:')

arr = []
for i in reversed(a):
	arr.append(i)
result = ''.join(arr)
print(result)

print('способ 3:')

result = a[::-1]
print(result)

print('способ 4:')

result = ''.join(list(reversed(a)))
print(result)

###################################
# Интересные варианты
###################################
print('\nИнтересеые варианты\n')


def rever(string):
	return ''.join(reversed(list(string)))


print(rever(a))


def insert_str(string):
	result = []
	for i in string:
		result.insert(0, i)

	return ''.join(result)


print(insert_str(a))

print('\nЗадание 2: подсчет глассных\n')
'''
УСЛОВИЕ:
подсчет гласных букв в строке.
Примечание:
- для простоты на вход принимаем строку из букв латинского алфавита;
- набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
- программа должна быть нечувствительна к регистру.
Пример:
s = "hApPyHalLOweEn!"
...
print result
> 5
'''

s = 'aSdasdfeOoO'  # вх строка
b = ('a', 'e', 'i', 'o', 'u')  # набор гласных букв

result = 0
for i in s.lower():
	for j in b:
		if i == j:
			result += 1
print(result)

###############################
# Интересный вариант
###############################
print('Интересный вариант')


def count_gl(str, arr):
	count = 0
	for i in str:
		if i.lower() in arr:
			count += 1
	return count


print(count_gl(s, b))

print('\nЗадание 3: подсчет вхождений подстроки\n')
'''
УСЛОВИЕ:
Реализовать подсчеты количества вхождений подстроки "wow" в строке.
ВХОД: строка
ВЫХОД: число вхождений подстроки "wow"
Пример:
s = "wowhatamanwowowpalehche"
...
> 3
'''

# Error: подумать, не выводит 3 значения
s = 'wowsdsdsdfdfwowowdfdsfds'
result = s.count('wow')
print(result)

#########################################
# Интересный вариант
#########################################
print('Интересный вариант')

wow = 0
for i, k in enumerate(s, 1):
	if s[i - 1:i + 2] == 'wow':
		wow += 1

print(wow)

print('\nЗадание 4: упорядочная подстрока.\n')
'''
УСЛОВИЕ:
Построить функционал который будет находить в строке подстроку максимальной длины, в которой буквы упорядочены в
алфавитном порядке.
ВХОД: строка
ВЫХОД: подстрока
Пример:
s = "sabrrtuwacaddabra"
...
> "abrrtuw"
'''
s = "sabrrtuwacaddabra"

final_out = ''
output = ''
prev = ''

for cur in s:
	if cur >= prev:  # сортируем с большего к меньшему
		output += cur
		if len(final_out) < len(output):  # сортировка по длине
			final_out = output
	else:
		output = cur  # алфавит сначала
	prev = cur
print(final_out)

#########################################
# Интересный вариант
#########################################
print('Интерсный вариант')


def podstr(str):
	prev = str[0]
	output = str[0]

	for i, k in enumerate(str):
		if str[i] >= prev[-1]:
			prev += str[i]
			if len(prev) > len(output):
				output = prev
		else:
			prev = str[i]
	return output


print(podstr(s))

print('\nЗадание 5: определение типа.\n')
'''
УСЛОВИЕ:
функция, которая принимает объект и выводит строку с наименованием типа этого объекта.
Пример:
typer(666) == "int"
typer("666") == "str"
typer(typer) == "function"
'''


def typer_2(arg):
	return type(arg).__name__  # возвращает имя объекта


print(typer_2(123))

result = lambda arg: type(arg).__name__
print(result('sddsd'))

print('\nЗадание 6: А & B.\n')
'''
УСЛОВИЕ:
Написать фрагмент python кода, который будет анализировать две переменные (А и В), которые могут быть типа "str" или "int".
В зависимости от значения переменных код должен выводить на печать ОДНО из следующих сообщений:
- "получена строка" - если хотя бы одна из переменных является строкой;
- "больше" - если А больше В;
- "равны" - если значения переменных равны;
- "меньше" - если А меньше В.
'''
a = 10
b = 9
'''
if type(a) == str or type(b) == str:
    result = 'Получена строка'
elif a > b:
    result = 'больше'
elif a < b:
    result = 'меньше'
else:
    result = 'равны'

print(result)
'''
if type(a) == type(b) == int:  # type('') is str
	if a > b:
		result = 'больше'
	elif a < b:
		result = 'меньше'
	else:
		result = 'равны'
else:
	result = 'Получена строка'

print(result)

print('\nЗадание 7: уникальный набор.\n')
'''
УСЛОВИЕ:
Реализовать функцию, которая принимает список елементов и убирает из него все дубликаты (формирует список уникальных
элементов).
Сделать вариант с сохранением порядка следования элементов и вариант, в кот. сортировка элементов не принципиальна.
Пример:
а) assert unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")]
б) assert unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]) == [2, "a", 5, (1, "a")]
'''
tmp = ["a", 5, 2, 5, (1, "a"), "a"]


def ordered(arr):
	m = []
	for i in arr:
		if i not in m:  # входит ли строка (i не в m)
			m.append(i)
	return m


print(ordered(tmp))


def unique_disordered(arg):
	return set(tmp)


print(unique_disordered(tmp))

print('\nЗадание 8: каждый третий.\n')
'''
УСЛОВИЕ:
Реализовать функционал который принимает кортеж и возвращает прореженный кортеж, оставляя только каждый третий элемент.
Реализовать задачу двумя разными вариантами.
Пример:
t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')
...
> (3,6,9,'b')
'''
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')

print('способ 1')

result = t[2::3]
print(result)

print('способ 2')

result = []
for k, v in enumerate(t, 1):
	if k % 3 == 0:
		result.append(v)
print(tuple(result))

# Задание 9: XYZ.
print('\nЗадание 9: XYZ.\n')
'''
УСЛОВИЕ:
Написать функционал без использования каких-ли   бо условных выражений, а применив встроенные функции min() и max(),
который принимает три аргумента - числа X, Y, Z и возвращает один из вариантов в порядке возрастания значимости:
- X, если Y < X;
- Z, если Y > Z;
- Y, при ином раскладе.
'''


def min_max(x, y, z):
	return min(max(x, y), z)


print(min_max(0, 3, 4))
