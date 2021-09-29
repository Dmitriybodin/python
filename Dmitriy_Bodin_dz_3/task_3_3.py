# Task 3

def thesaurus(*names):
    names_dict = {}
    for name in names:
        names_dict.setdefault(name[0], [])
        names_dict[name[0]].append(name)
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))