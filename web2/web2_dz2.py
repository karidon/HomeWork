# -*- coding: utf-8 -*-

'''
Задание 2: Симметрия.

УСЛОВИЕ:
Фрагмент кода, который принимает строку и определяет симметрична ли строка.
(Возвращает True или False).

Пример:
"abba" >> True
"arbat" >> False
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-20'


def symmetry(string):
	i = len(string) // 2
	return True if string[:i] == string[:i - 1:-1] else False
