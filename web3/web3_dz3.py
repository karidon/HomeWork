# -*- coding: utf-8 -*-

'''
Задание 3: Реверс'em!

УСЛОВИЕ:
Изменить в тексте порядок следования:
- букв в словах;
- слов в предложениях;
- предложений в тексте.
Вывести модифицированный текст.

Текст:
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum
dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna
dictum porta.
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-30'


def reversem(text):
	'''
	Изменяет порядок следования текст
	- букв в словах;
	- слов в предложениях;
	- предложений в тексте.
	:param text: str
	:return: str
	'''
	a = []
	str = text.strip(' \n\t')
	for i in str.split('.'):
		a.append(i[::-1])
	out = ''
	for j in a[::-1]:
		out += j
	return out
