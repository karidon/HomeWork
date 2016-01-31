# -*- coding: utf-8 -*-

'''
Задание 3: Триделение.

УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и возвращает словарь вида:
{число: boolean}, где: boolean - True или False в зависимости делится ли число на 3
без остатка.

Пример:
[3,7,12] >> {3:True, 12:True, 7:False}
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-20'


def tridelta(arg):
	m = {}
	for i in arg:
		if i % 3 == 0:
			a = True
		else:
			a = False
		m[i] = a
	return m
