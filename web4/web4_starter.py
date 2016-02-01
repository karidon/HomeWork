# -*- coding: utf-8 -*-


'''
Основной скрипт запуска ДЗ №4.

Данный скрипт призван запускать на выполнение домашнее задание №4.
Также выполняется комплекс тестов из модуля набора тестов.
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-01'

import web4_dz1

from web4_tests import tests_for_web4_dz1

INPUT_1 = 'ABCda'


def runner():
	'''Запускает выполненние всех задач'''
	print(INPUT_1, '>>\n', web4_dz1.frequency_letters(INPUT_1))


if __name__ == '__main__':
	runner()
	tests_for_web4_dz1()
