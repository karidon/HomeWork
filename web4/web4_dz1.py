# -*- coding: utf-8 -*-

'''
Задание 1: Частота буквы.
 
УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква встречается в тексте.
 
Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.
 
Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-01'


def frequency_letters(text):
	'''
	Подсчитывает процентное соотношениек букв в тексте
	:param text: str
	:return: dict
	'''
	tmp = text.strip('.,?!-+=:;\'\"{}#').casefold()
	tmp = ''.join(tmp.split())
	l = len(tmp)
	dic = {}
	# Считает количество одной букв в тексте
	for v in tmp:
		dic[v] = dic.get(v, 0) + 1
	# Считает процентное соотношение букв в тексте
	for key, value in dic.items():
		dic[key] = round(((value / l) * 100), 1)
	return dic


###################################################
# Способ PyBursa
###################################################

import string
from collections import Counter


def percentage_1(text):
	u"""Решение через простые итерации."""
	symbol_counts = {}
	for symbol in text.lower():
		if symbol in string.ascii_lowercase:
			symbol_counts[symbol] = symbol_counts.setdefault(symbol, 0) + 1

	all_letters = float(sum(symbol_counts.values()))
	symbol_percentage = {}
	for k, v in symbol_counts.items():
		symbol_percentage[k] = round(v / all_letters * 100, 1)
	return symbol_percentage


def percentage_2(text):
	u"""Решение через инструменты стандартной библиотеки."""
	symbol_counts = Counter(filter(
		lambda s: s in string.ascii_letters, text.lower()))
	all_letters = float(sum(symbol_counts.values()))
	items = symbol_counts.items()
	symbol_percentage = {k: round(v / all_letters * 100, 1) for k, v in items}
	return symbol_percentage
