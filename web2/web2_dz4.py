# -*- coding: utf-8 -*-

'''
Задание 4: Чет-нечет.

УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и фильтрует его по четным (удаляет нечетные),
если количество элементов в списке является четным и наоборот (удаляет четные, если элементов изначально нечетное количество).

Пример:
[3,7,12] >> [3,7]
[3,7,12,7] >> [12]
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-20'


def even_odd(m):
	if len(m) % 2 == 0:
		return list(filter((lambda x: x % 2 == 0), m))
	return list(filter((lambda x: x % 2 == 1), m))
