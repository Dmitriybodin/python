# Task 1

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
    return nums_dict.get(eng_num)


print(num_translate('one'))
print(num_translate('eight'))
print(num_translate('eleven'))

