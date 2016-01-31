# -*- coding: utf-8 -*-

'''
Задание 1: И снова гласные.

УСЛОВИЕ:
Посчитать количество гласных в каждом слове текста.
Вывести максимальное количество гласных в одном слове.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus.
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
Гласные: A, E, I, O, U, Y
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-30'


def number_glasnik(text):
	'''
	Считает максимальное количество гласных в слове
	:param text: входящий текст
	:return: максимальное количесвто глассных в одном слове
	'''
	glasn = ('A', 'E', 'I', 'O', 'U', 'Y')
	arr = text.upper().split()

	# считаем сколько глассных в слове
	m = []
	for i in arr:
		m.append([i, sum(j in glasn for j in i)])

	# определяем максимальное количество в одном слове
	tmp = m[0][1]
	for i, k in enumerate(m):
		if m[i][1] > tmp:
			tmp = m[i][1]
			out = k
	return out
