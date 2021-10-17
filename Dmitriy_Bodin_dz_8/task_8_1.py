# Task 1

import re

EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    found_info = EMAIL.findall(email)[0]
    if found_info:
        login, domain = found_info
    else:
        raise ValueError(f'wrong email: {email}')
    print({'username': login, 'domain': domain})


email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
