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
	# TODO 1: Переделать
	assert web3_dz3.reversem(
		"Lorem ipsum dolor sit amet, consectetur adipiscing elit.	Nulla quis "
		"lorem ut libero malesuada feugiat. " \
		"Lorem ipsum dolor sit amet, consectetur adipiscing elit.	Donec "
		"rutrum congue leo eget malesuada.	" \
		"Cras ultricies ligula sed magna dictum porta."
	) == "atrop mutcid angam des alugil seicirtlu sarC	adauselam tege oel eugnoc " \
	     "murtur cenoD	tile gnicsipida rutetcesnoc ,tema tis rolod muspi meroL " \
	     "taiguef adauselam orebil tu merol siuq alluN	tile gnicsipida " \
	     "rutetcesnoc ,tema tis rolod muspi meroL"


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
