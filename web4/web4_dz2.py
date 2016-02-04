# -*- coding: utf-8 -*-

'''
Задание 2: Послесловие...
 
УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в случае, если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться на середине (исключение первое слово),
и в конце нужно добавить троеточие ("...").
 
Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.
 
Пример:
text = "Proin eget tortor risus."
limit = 24
output = "Proin eget tortor risus."
limit = 23
output = "Proin eget tortor..."
limit = 13
output = "Proin eget..."
limit = 6
output = "Pro..."
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-04'


def epilogue(text, limit=24):
	'''
	Обрезает текст по limit
	:param text: вх текс
	:param limit: ограничение текста
	:return: обрезанный текст по limit
	'''
	arr = text.split()
	s = text[:limit]
	count = 0
	if len(text) <= limit:
		s = text
	elif len(text) > limit > (len(arr[0]) + 1):
		for value in text[limit::-1]:
			if value != ' ':
				count += 1
			else:
				s = text[:limit - count] + '...'
				break
	else:
		s = text[:limit - 3] + '...'
	return s
