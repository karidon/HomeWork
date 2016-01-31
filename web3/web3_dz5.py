# -*- coding: utf-8 -*-

'''
Задание 5: Псевдосумма.

УСЛОВИЕ:
Принимать любое натуральное число.
Выдавать сумму цифр, из которых число состоит.
Не использовать оператор "+" и встроенную функцию sum().

Пример:
456 >> 15
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-30'

from functools import reduce


def psevdosumma(number=0):
	'''
	Выдает сумму цифр из которых стостоит число
	:param number: натуральное число
	:return: сумма цифр
	'''
	arr = []
	m = list(str(abs(number)))
	for v in m:
		arr.append(int(v))
	return reduce((lambda x, y: x.__add__(y)), arr)
