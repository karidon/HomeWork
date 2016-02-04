# -*- coding: utf-8 -*-


'''
Основной скрипт запуска ДЗ №4.

Данный скрипт призван запускать на выполнение домашнее задание №4.
Также выполняется комплекс тестов из модуля набора тестов.
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-04'

import web4_dz1
import web4_dz2

from web4_tests import tests_for_web4_dz1, tests_for_web4_dz2

INPUT_1 = 'ABCda'
INPUT_2 = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.' \
          ' Donec rutrum congue leo eget malesuada.'


def runner():
	'''Запускает выполненние всех задач'''
	print(INPUT_1, '>>\n', web4_dz1.frequency_letters(INPUT_1))
	print(INPUT_2, '>>\n', web4_dz2.epilogue(INPUT_2))


if __name__ == '__main__':
	runner()
	tests_for_web4_dz1()
	tests_for_web4_dz2()
