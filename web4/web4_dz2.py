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


def epilogue(text, limit=0):
	'''
	Обрезает текст по limit
	:param text: текст
	:param limit: ограничение текста
	:return: обрезанный текст по limit
	'''
	arr = text.split()
	s = text[:limit]
	eliment = '...'
	count = 0
	if not limit or len(text) <= limit:
		s = text
	elif len(text) > limit > (len(arr[0]) + 1):
		for value in text[limit::-1]:
			if value != ' ':
				count += 1
			else:
				s = text[:limit - count] + eliment
				break
	else:
		s = text[:limit - 3] + eliment
	return s


###################################################
# способ PyBursa
##################################################

def ellipsis_1(text, limit=0):
	"""Решение через индексы концов слов..."""
	assert limit not in [1, 2], "Invalid limit argument!"
	ellipsis = "..."
	if not limit or limit >= len(text):
		return text
	trimmed_text = ""
	for i, word in enumerate(text.split()):
		trimmed_text += word + " "
		if len(trimmed_text[:-1] + ellipsis) > limit:
			if i == 0:
				return word[: limit - len(ellipsis)] + ellipsis
			return trimmed_text[:-len(word) - 2] + ellipsis
