# Task 4

def thesaurus_adv(*names_surnames):
    names_surnames_dict = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        names_surnames_dict.setdefault(surname[0], {})
        names_surnames_dict[surname[0]].setdefault(name[0], [])
        names_surnames_dict[surname[0]][name[0]].append(name_surname)
    return names_surnames_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))