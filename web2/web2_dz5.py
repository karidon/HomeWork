# -*- coding: utf-8 -*-

'''
Задание 5: Сепаратор.

УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и модифицирует его следующим образом:
- в начале списка идут нечетные числа в порядке возрастания,
- далее идут четные числа в порядке убывания.

Пример:
[1,4,8,6,3,7,1] >> [1,1,3,7,8,6,4]
'''

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-01-20'


def separator(m):
	'''
	arr1 = []
	arr2 = []
	for i in m:
		if i%2 == 0:
			arr1.append(i)
		else:
			arr2.append(i)
	arr1.sort(reverse=True)
	arr2.sort()
	'''
	arr1 = sorted([i for i in m if i % 2 == 0], reverse=True)
	arr2 = sorted(filter((lambda x: x % 2 == 1), m))
	return arr2 + arr1
