# -*- coding: utf-8 -*-

'''
Тесты на ДЗ №4
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-04'

import web4_dz1
import web4_dz2


def tests_for_web4_dz1():
	'''Тесты задачи 1'''
	assert web4_dz1.frequency_letters("A") == {'a': 100.0}

	assert web4_dz1.frequency_letters("ABCda") == {
		'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0
	}

	assert web4_dz1.frequency_letters("AsBCda") == {
		'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7, 's': 16.7
	}

	assert web4_dz1.frequency_letters("q TyU#!{}.") == {
		'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0
	}

	assert sum(web4_dz1.frequency_letters("q TyU#!{}.").values()) == 100.0

	assert web4_dz1.frequency_letters("A") == {'a': 100.0}

	assert web4_dz1.frequency_letters("ABCda") == {
		'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0
	}
	assert web4_dz1.frequency_letters("AsBCda") == {
		'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7, 's': 16.7
	}
	assert web4_dz1.frequency_letters("q TyU#!{}.") == {
		'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0
	}
	assert sum(web4_dz1.frequency_letters("q TyU#!{}.").values()) == 100.0
	assert web4_dz1.frequency_letters("приве") == {
		'п': 20.0, 'р': 20.0, 'и': 20.0, 'в': 20.0, 'е': 20.0
	}


def tests_for_web4_dz2():
	"""Тесты задачи 2"""
	text = "Proin eget tortor risus."
	assert web4_dz2.epilogue(text) == "Proin eget tortor risus."
	assert web4_dz2.epilogue(text, 24) == "Proin eget tortor risus."
	assert web4_dz2.epilogue(text, 23) == "Proin eget tortor..."
	assert web4_dz2.epilogue(text, 13) == "Proin eget..."
	assert web4_dz2.epilogue(text, 6) == "Pro..."
