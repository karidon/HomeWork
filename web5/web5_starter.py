# -*- coding: utf-8 -*-

'''
Основной скрипт запуска ДЗ №5.

Данный скрипт призван запускать на выполнение домашнее задание №5.
Также выполняется комплекс тестов из модуля набора тестов.
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-11'

import web5_dz1

from web5_tests import tests_for_web5_dz1


def runner():
	'''Запускает выполненние всех задач'''
	korkin = web5_dz1.Person("Korkin", "Vinalya", "1988-12-20")
	print(korkin.get_age())
	print(korkin.get_fullname())


if __name__ == '__main__':
	runner()
	tests_for_web5_dz1()
