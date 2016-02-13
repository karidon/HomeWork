# -*- coding: utf-8 -*-

'''
Задание 1: классный Человек.
 
УСЛОВИЕ:
 
Реализовать класс Person, который отображает запись в книге контактов.
 
Класс имеет 4 атрибута:
- surname - строка - фамилия контактам (обязательный)
- first_name - строка - имя контакта (обязательный)
- nickname - строка - псевдоним (опциональный)
- birth_date - объект datetime.date (обязательный)
 
Каждый вызов класса должен создавать экземпляр (инстанс) класса с указанными
атрибутами.
 
Также класс имеет 2 метода:
- get_age() - считает возраст контакта в полных годах на дату вызова и
возвращает строку вида: "27";
- get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя)
контакта;

Примечание:
1) смотрите документацию по модулю datetime;
2) при создании атрибута birth_date из строки типа "2014-12-31" необходимо:
- определить какая информация нужна для создания объекта datetime.date,
- получить эти данные из строки - разобрать ее (достать из нее отдельно,
год, месяц, число),
- на основании этой информации создать специальный объект datetime.date,
- поместить этот спец.объект в атрибут экземпляра класса;
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-08'

from datetime import date


class Person(object):
	'''
	Реализует запись в книге контактов
	'''

	def __init__(self, surname, first_name, birth_date, nickname=None):
		'''

		:param surname: строка - фамилия контактам (обязательный)
		:param first_name: строка - имя контакта (обязательный)
		:param birth_date: день рождения
		:param nickname: строка - псевдоним (опциональный)
		:return:
		'''
		self.surname = surname
		self.first_name = first_name
		self.nickname = nickname

		# Разбираем строку birth_date
		# TODO: подумать над вариантами
		_arr = birth_date.split('-')
		_year = int(_arr[0])
		_month = int(_arr[1])
		_day = int(_arr[2])

		self.birth_date = date(_year, _month, _day)

	def get_age(self):
		'''
		Считает возраст контакта в полных годах на дату вызова
		:return: возвращает строку вида: "27"
		'''
		max = date.today()
		res = max - self.birth_date
		return str(res.days // 365)

	def get_fullname(self):
		'''
		:return: строку, отражающая полное surname + first_name (фамилия + имя)
		контакта
		'''
		return self.surname + ' ' + self.first_name