# -*- coding: utf-8 -*-

'''
Тесты на ДЗ №3
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-30'

import web3_dz1
import web3_dz2
import web3_dz3
import web3_dz5
import web3_dz6


def tests_for_web3_dz1():
	'''Тесты задачи 1'''
	assert web3_dz1.number_glasnik(
		"Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta." \
		" Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus " \
		"convallis quis ac lectus. Donec rutrum congue leo eget malesuada.") == \
	       ['MALESUADA.', 5]


def tests_for_web3_dz2():
	'''Тесты задачи 2'''
	assert web3_dz2.long_word(
		"Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta." \
		" Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus " \
		"convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
	) == ['malesuada', 'convallis', 'Curabitur', 'ultricies']


def tests_for_web3_dz3():
	'''Тесты задачи 3'''
	assert web3_dz3.reversem(
		'Hello world! I am sorry.') == 'yrros ma I !dlrow olleH'


def test_for_web3_dz4():
	pass


def tests_for_web3_dz5():
	'''Тесты задачи 5'''
	assert web3_dz5.psevdosumma(456) == 15
	assert web3_dz5.psevdosumma(-456) == 15
	assert web3_dz5.psevdosumma() == 0


def tests_for_web3_dz6():
	'''Тест задачи 6'''
	assert web3_dz6.prime_numbers() == [2, 3, 5, 7, 11, 13, 17, 19]
	assert web3_dz6.prime_numbers(5) == [2, 3, 5]
	assert web3_dz6.prime_numbers(-5) == [2, 3, 5]
