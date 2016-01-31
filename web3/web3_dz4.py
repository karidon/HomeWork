# -*- coding: utf-8 -*-


print('Задание 4: Imports.')
'''
УСЛОВИЕ:
Произвести импортирование модулей стандартной библиотеки Python: "os" и "sys".
Вывести справку по всем функциям каждого модуля.
'''

import os, sys


def informations(libraly):
	'''
	Принимает название модуля и формирует справку по всем функциям принимаемого модуля
	:param libraly: название модуля
	:return: словарь
	'''
	dic = {}
	for i in dir(libraly):
		dic[i] = i.__doc__
	return dic


def output(dic):
	'''
	Выводит функции с описанием
	:param modul:словарь с именем функции и описание ее
	:return:
	'''
	for k, v in sorted(dic.items()):
		print('-' * 60)
		print('\nИмя функции: {0}\n\nОписание функции: \n{1}'.format(k, v))


if __name__ == '__main__':
	s = informations(sys)
	output(s)
	o = informations(os)
	output(o)
