# -*- coding: utf-8 -*-

'''
Задание 6: Простые числа. (бонусное)

УСЛОВИЕ:
Вывести на печать 10000 первых натуральных простых чисел.
Напомню, что это те, которые делятся без остатка не себяi и 1,
начиная с числа 2.
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-30'


def prime_numbers(number=20):
	'''
	Выводит натуральные простые числа.
	:param numbers: количество чисел.
	:return: список найденых протостых чисел.

	'''
	number = abs(number)
	# Заполняем словарь числами.
	dic = {i: True for i in range(2, number + 1)}

	# Высчитваем l*l < numbers.
	arr = [l for l in dic.keys() if l * l <= number]

	# Считает натуральные простые числа.
	for j in dic.keys():
		for i in arr:
			if j == i:
				continue
			else:
				if j % i == 0:
					dic[j] = False
	# Список натуральный простых чисел.
	out_list = [key for key in dic.keys() if dic[key] == True]
	return out_list


def first(num):
	'''
	Выводит количество натуральных простых чисел
	:param num: количество
	:return: список чисел
	'''
	# TODO 1: Функция зависает если выводит 1000
	tmp = 50
	control = True

	while control:
		arr = prime_numbers(tmp)
		if len(arr) != num:
			tmp += 1
		else:
			control = False
	yield arr
