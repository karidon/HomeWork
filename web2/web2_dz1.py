# -*- coding: utf-8 -*-

'''
Задание 1: Квадраты.

УСЛОВИЕ:
Фрагмент кода, который принимает набор (список, кортеж) чисел и возвращает набор
ТОГО ЖЕ типа со значениями квадратов этих чисел.

Пример:
[1,2,3] >> [1,4,9]
(1,2,3) >> (1,4,9)
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-20'


def value_square(arg):
	return type(arg)(map(lambda x: x * x, arg))