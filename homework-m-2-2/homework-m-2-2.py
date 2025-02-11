#Декоратор в python

"""
Создайте файл latin.py напишите класс-декоратор ToLatin, который
работает с функциями, принимающими строковое значение. Данный
декоратор должен проверять если декорируемая функция возвращает
строку на кириллице, то декоратор преобразовывает ее в латиницу,
используя следующий словарь для замены русских букв на
соответствующее латинское написание:

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 
'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 
'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 
'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 
'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 
'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 
'э': 'e', 'ю': 'yu', 'я': 'ya'}

Также данный декоратор должен сам принимать аргумент is_login.
Если is_login=True, то декорированная функция должна возвращать
значение пригодное для использования в качестве логина, то есть
без пробелов, вместо пробелов использовать «_». Если is_login=False,
то декорированная функция должна возвращать преобразованную строку.
Замены делать без учета регистра (исходную строку перевести в нижний
регистр – малые буквы).

Пример №1:
Входные данные
@ToLatin(is_login=False)
     def some_func(name, surname):

         return f’{surname} {name}’

some_func(‘Айбек’, ‘Бакиев’)

Выходные данные:
Функция возвращает aybek bakiev

Пример №2:
Входные данные
@ToLatin(is_login=True)
    def some_func(name, surname):
        return f’{surname} {name}’

some_func(‘Айбек’, ‘Бакиев’)

Выходные данные: Функция возвращает aybek_bakiev
"""
   
from latin import ToLatin

@ToLatin(is_login=False)
def some_func(name, surname):
    return f'{name} {surname}'

print(some_func('Айбек', 'Бакиев'))  # Вывод: aybek bakiev 

@ToLatin(is_login=True)
def some_func(name, surname):
    return f'{name} {surname}'

print(some_func('Айбек', 'Бакиев'))  # Вывод: aybek_bakiev

