# -*- coding: utf-8 -*-


'''
Основной скрипт запуска ДЗ №2.

Данный скрипт призван запускать на выполнение домашнее задание №2.
Также выполняется комплекс тестов из модуля набора тестов.
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

from web2_tests import tests_for_web2_dz1, tests_for_web2_dz2
from web2_tests import tests_for_web2_dz3, tests_for_web2_dz4
from web2_tests import tests_for_web2_dz5, tests_for_web2_dz6
from web2_tests import tests_for_web2_dz7, tests_for_web2_dz8
from web2_tests import tests_for_web2_dz9



INPUT_1 = [1,2,3]
INPUT_2 = 'abba'
INPUT_3 = [3,7,12]
INPUT_4 = [3,7,12,7]
INPUT_5 = [1,4,8,6,3,7,1]
INPUT_6 = {'a': 1, 3: [1,5], 'e': 'abc', '6': []}
INPUT_7 = [1,4,8,6,3,7,1]
INPUT_8 = (1,4,8,6,3,7,1)
INPUT_9 = [[1],[4,8],[6,3,7],[1,3]]


def runner():
	'''Запускает выполнение всех задач'''
	print(INPUT_1, '>>\n', web2_dz1.value_square(INPUT_1))
	print(INPUT_2, '>>\n', web2_dz2.symmetry(INPUT_2))
	print(INPUT_3, '>>\n', web2_dz3.tridelta(INPUT_3))
	print(INPUT_4, '>>\n', web2_dz4.even_odd(INPUT_4))
	print(INPUT_5, '>>\n', web2_dz5.separator(INPUT_5))
	print(INPUT_6, '>>\n', web2_dz6.classifier(INPUT_6))
	print(INPUT_7, '>>\n', web2_dz7.separator_advanced(INPUT_7))
	print(INPUT_8, '>>\n', web2_dz8.duplex(INPUT_8))
	print(INPUT_9, '>>\n', web2_dz9.shrew(INPUT_9))


if __name__ == '__main__':
	runner()
	tests_for_web2_dz1()
	tests_for_web2_dz2()
	tests_for_web2_dz3()
	tests_for_web2_dz4()
	tests_for_web2_dz5()
	tests_for_web2_dz6()
	tests_for_web2_dz7()
	tests_for_web2_dz8()
	tests_for_web2_dz9()

