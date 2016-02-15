# -*- coding: utf-8 -*-

"""
Основной скрипт запуска ДЗ.
Данный скрипт призван запускать на выполнение домашнее задание #6.
"""

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-11'

from web6_dz1 import modifier


def runner():
	"""Запускает выполнение всех задач"""
	print('Modifying file...')
	modifier('data.csv')
	print('Modified successfully!')


if __name__ == '__main__':
	runner()
