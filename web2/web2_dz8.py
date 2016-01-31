# -*- coding: utf-8 -*-

'''
Задание 8: Двууровневый кортеж. (бонусное)

УСЛОВИЕ:
Фрагмент кода, который принимает кортеж любых чисел и модифицирует его
в кортеж кортежей по два элемента (парами).

Пример:
(1,4,8,6,3,7,1) >> ((1,4),(8,6),(3,7),(1,))
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-20'


def duplex(arg):
	# cам не догодался
	'''
	arr = []
	for i in range(0, len(arg), 2):
		arr.append(arg[i:i+2])
	return tuple(arr)
	'''
	return tuple([arg[i:i + 2] for i in range(0, len(arg), 2)])
