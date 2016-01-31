# -*- coding: utf-8 -*-

# Задание 10: интерактивный подсчет гласных.
'''
УСЛОВИЕ:
Написать программу (python script), которая при запуске будет запрашивать пользователя ввести произвольную строку и
выдавать в ответе количество гласных букв.
Примечание:
- для ручного ввода используем встроенную функцию raw_input();
- для простоты на вход принимаем строку из букв латинского алфавита;
- набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
- программа должна быть нечувствительна к регистру.
ВХОД: строка (ручной ввод пользователем)
ВЫХОД: строка вида:
"The string contains 2 vowels" - если гласные присутствуют,
"The string doesn't contain vowels" - в противном случае.
Пример:
python ivowels.py - запуск
Вывод:
"Please, enter your string: "
"wHAt Do yOU wANt fRom ME?"
"The string contains 7 vowels"
"Continue? (yes/no) "
"maybe"
"Please, enter corrent answer. Continue? (yes/no) "
"yes"
"Hurray!"
"Please, enter your string: "
"HHHMMMMM..."
"The string doesn't contain vowels"
"Continue? (yes/no) "
"no"
"It was nice to count your vowels!"
'''


# s = input('Please, enter your string: ')

def glass(str):
	'''
    Считает сколько гласных букв находится в строке
    :param str: входящая строка
    :return: возвращает количество гласных букв
    '''
	tup = ('a', 'e', 'i', 'o', 'u')  # гласные буквы
	count = 0

	for i in str.lower():
		for j in tup:
			if i == j:
				count += 1
	return count


if __name__ == '__main__':

	a = True

	while a:
		s = input('Please, enter your string: ')

		i = glass(s)

		if i == 0:
			print("The string doesn't contain vowels")
		else:
			print("The string contains {0} vowels".format(i))

		s = input("Continue? (yes/no) ").lower()

		while True:
			if s == 'no':
				a = False
				break
			elif s == 'yes':
				print('Hurray!')
				break
			else:
				s = input(
					"Please, enter corrent answer. Continue? (yes/no) ").lower()
	else:
		print('It was nice to count your vowels!')
