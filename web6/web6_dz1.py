# -*- coding: utf-8 -*-

'''
Задание 6.1: вычитка по полной.
 
УСЛОВИЕ:
дан файл с данными: HomeWork/web6/data.csv
 
Написать функцию modifier(filename), которая принимает имя файла и должна:
- вычитать данные из переданного файла;
- создать объекты класса Person на основании полученных данных;
- модифицировать данные в файле:
а) добавить графу полного имени (fullname) после графы с именем (name)
б) добавить графу с возрастом (age) в конец.
 
На выходе получить файл, расширенный указанным образом.
 
Примечание:
1) смотрите документацию по модулю csv;
(https://docs.python.org/2/library/csv.html?highlight=csv#module-csv)
 
 
Запускать через скрипт (HomeWork/.../web6/web6_starter.py)
 
Тестов в этом задании не предусмотрено.
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-02-11'

import csv

from web5.web5_dz1 import Person


def modifier(filename):
	'''
	Модифицирует данные в файле
	:param filename: str
	:return: csv file
	'''
	arr = []
	with open(filename, 'r') as fp:
		csv_obgect = csv.DictReader(fp)
		for row in csv_obgect:
			row['id'] = Person(row['surname'], row['name'], row['birthdate'],
			                   row['nickname'])
			arr.append(row['id'])

	with open(filename, 'w', newline='') as fp:
		fieldnames = ['id', 'surname', 'name', 'fullname', 'birthdate',
		              'nickname', 'age']
		writer = csv.DictWriter(fp, fieldnames=fieldnames)
		writer.writeheader()

		# Модификация файла
		for i, person in enumerate(arr):
			writer.writerow(
				{'id': i + 1, 'surname': person.surname,
				 'name': person.first_name,
				 'fullname': person.get_fullname(),
				 'birthdate': person.birth_date,
				 'nickname': person.nickname, 'age': person.get_age()})
