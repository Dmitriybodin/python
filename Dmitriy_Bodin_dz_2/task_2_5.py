#Task 5

goods = [57.8, 46.51, 54, 84.71, 38.29, 0.99, 65.34, 251, 8, 12.34]
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп',end=', ')
print('\n')


goods = [57.8, 46.51, 54, 84.71, 38.29, 0.99, 65.34, 251, 8, 12.34]
print(id(goods))
goods.sort()
print(id(goods))
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')
print('\n')


goods = [57.8, 46.51, 54, 84.71, 38.29, 0.99, 65.34, 251, 8, 12.34]
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')