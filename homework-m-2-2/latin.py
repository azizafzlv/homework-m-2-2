#класс декоратор для замены букв на латиницу


class ToLatin:
    def __init__(self, is_login=False):
        self.is_login = is_login

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, str):
                result = result.lower()

                t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 
                     'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 
                     'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 
                     'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 
                     'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 
                     'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 
                     'э': 'e', 'ю': 'yu', 'я': 'ya'}

                for char in result:
                    if char in t:
                        result = result.replace(char, t[char])

                if self.is_login:
                    result = result.replace(' ', '_')

            return result

        return wrapper
    
