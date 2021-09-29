#Task 4

awry_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in awry_list:
    print('Привет,', position.split()[-1].title(), end='')
    print('!')