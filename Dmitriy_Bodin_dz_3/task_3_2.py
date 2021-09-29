# Task 2

nums_dict = {'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}


def num_translate(eng_num):
    if eng_num[0].isupper():
        num_word = eng_num.lower()
        return nums_dict.get(num_word).title()
    else:
        return nums_dict.get(eng_num)


print(num_translate('One'))
print(num_translate('eight'))
print(num_translate('eleven'))