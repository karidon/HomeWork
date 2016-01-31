# -*- coding: utf-8 -*-


'''
Основной скрипт запуска ДЗ №3.

Данный скрипт призван запускать на выполнение домашнее задание №4.
Также выполняется комплекс тестов из модуля набора тестов.
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-30'

import web3_dz1
import web3_dz2
import web3_dz3
import web3_dz5
import web3_dz6

from web3_tests import tests_for_web3_dz1, tests_for_web3_dz2
from web3_tests import tests_for_web3_dz3, tests_for_web3_dz5
from web3_tests import tests_for_web3_dz6

INPUT_1 = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta." \
          " Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus " \
          "convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
INPUT_2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.	Nulla quis lorem ut libero malesuada feugiat. " \
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit.	Donec rutrum congue leo eget malesuada.	" \
          "Cras ultricies ligula sed magna dictum porta."

INPUT_5 = 456
INPUT_6 = 1000


def runner():
	'''Запускает выполненние всех задач'''
	print(INPUT_1, '>>\n', web3_dz1.number_glasnik(INPUT_1))
	print(INPUT_1, '>>\n', web3_dz2.long_word(INPUT_1))
	print(INPUT_2, '>>\n', web3_dz3.reversem(INPUT_2))
	print(INPUT_5, '>>\n', web3_dz5.psevdosumma(INPUT_5))
	print(INPUT_6, '>>\n', web3_dz6.prime_numbers(INPUT_6))


if __name__ == '__main__':
	runner()
	tests_for_web3_dz1()
	tests_for_web3_dz2()
	tests_for_web3_dz3()
	tests_for_web3_dz5()
	tests_for_web3_dz6()
