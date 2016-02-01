# -*- coding: utf-8 -*-

'''
Задание 2: Послесловие...
 
УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в случае, если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться на середине (исключение первое слово),
и в конце нужно добавить троеточие ("...").
 
Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.
 
Пример:
text = "Proin eget tortor risus."
limit = 24
output = "Proin eget tortor risus."
limit = 23
output = "Proin eget tortor..."
limit = 13
output = "Proin eget..."
limit = 6
output = "Pro..."
'''

