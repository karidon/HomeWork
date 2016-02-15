# -*- coding: utf-8 -*-

'''
Задание 2: Самое длинное слово.

УСЛОВИЕ:
Найти слово максимальной длины в тексте.
Вывести это слово. Если таких слов несколько - вывести все.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla
sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-30'


def long_word(text):
	'''
	Ищет максимальное длиное слова и выводит все максимальной длины слов
	:param text: str
	:return: str
	'''
	arr = text.strip('.,\'\"\n\t[]<>').split()

	# пузырковая сортировка
	for i in reversed(range(len(arr))):
		for j in range(1, i):
			if len(arr[j]) < len(arr[j - 1]):
				arr[j], arr[j - 1] = arr[j - 1], arr[j]
	arr.reverse()

	# выводим все максимальные слова
	for i in range(1, len(arr)):
		if len(arr[i - 1]) == len(arr[i]):
			m = arr[:i + 1]
		else:
			break
	return m
