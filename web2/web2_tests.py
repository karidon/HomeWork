# -*- coding: utf-8 -*-

'''
Тесты на ДЗ №2
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-20'


import web2_dz1
import web2_dz2
import web2_dz3
import web2_dz4
import web2_dz5
import web2_dz6
import web2_dz7
import web2_dz8
import web2_dz9


def tests_for_web2_dz1():
	'''Тесты задачи 1'''
	assert web2_dz1.value_square([1,2,3]) == [1,4,9]
	assert web2_dz1.value_square((1,2,3)) == (1,4,9)
	assert web2_dz1.value_square([-2,3,4]) == [4,9,16]


def tests_for_web2_dz2():
	'''Тесты задачи 2'''
	assert web2_dz2.symmetry('abddba') == True
	assert web2_dz2.symmetry('arbat') == False


def tests_for_web2_dz3():
	'''Тесты задачи 3'''
	assert web2_dz3.tridelta([3,7,12]) == {3:True, 12:True, 7:False}


def tests_for_web2_dz4():
	'''Тесты задачи 4'''
	assert web2_dz4.even_odd([3,7,12]) == [3,7]
	assert web2_dz4.even_odd([3,7,12,7]) == [12]


def tests_for_web2_dz5():
	'''Тесты задачи 5'''
	assert web2_dz5.separator([1,4,8,6,3,7,1]) == [1,1,3,7,8,6,4]


def tests_for_web2_dz6():
	'''Тесты задачи 6'''
	assert web2_dz6.classifier({'a': 1, 3: [1,5], 'e': 'abc', '6': []}) == \
	       {'str': 1, 'list': 2, 'int': 1}


def tests_for_web2_dz7():
	'''Тесты задачи 7'''
	assert web2_dz7.separator_advanced([1,4,8,6,3,7,1]) == [1,1,3,7,8,6,4]


def tests_for_web2_dz8():
	'''Тесты задачи 8'''
	assert web2_dz8.duplex((1,4,8,6,3,7,1)) ==((1,4),(8,6),(3,7),(1,))


def tests_for_web2_dz9():
	'''Тесты задачи 8'''
	assert web2_dz9.shrew([[1],[4,8],[6,3,7],[1,3]]) == [1,4,8,6,3,7,1,3]