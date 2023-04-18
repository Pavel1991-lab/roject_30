def to_uppercase(string):
    return string.upper()


def capitalize_first_letters(string):
    """
    Функция принимает на вход строку и возвращает строку, в которой первые буквы каждого слова заглавные.
    :param string: строка
    :return: строка с заглавными первыми буквами каждого слова
    """
    words = string.split()
    capitalized_words = []
    for word in words:
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)
    return " ".join(capitalized_words)