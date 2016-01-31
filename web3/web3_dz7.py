# -*- coding: utf-8 -*-


print("Задание 7: Реверс'em all! (бонусное)")
'''
УСЛОВИЕ:
Выполнить задание 3 с сохранением позиций:
- знаков препинания ("word," >> "drow,");
- Заглавных букв в начале предложения ("Word ..." >> "Drow ...").
=====================================================
'''


def reversem_all(text):
	'''
	Изменяет порядок следования текст:
	- букв в словах;
	- слов в предложениях;
	- предложений в тексте.
	:param text: техт
	:return: текст модифицированный

	'''
	# TODO 1: Надо подумать

	a = []
	str = text.strip(' \n\t')
	for i in str.split('.'):
		a.append(i[::-1])
	for j in a[::-1]:
		print(j + '.')


# str = text[::-1]





if __name__ == '__main__':
	s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.	Nulla quis lorem ut libero malesuada feugiat. " \
	    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.	Donec rutrum congue leo eget malesuada.	" \
	    "Cras ultricies ligula sed magna dictum porta."

	reversem_all(s)
