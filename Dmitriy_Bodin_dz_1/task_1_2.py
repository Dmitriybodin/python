# Task 2
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a. Вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» # будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
#
# b. К каждому элементу списка добавить 17 и заново вычислить
# сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#
# c. Решить задачу под пунктом b, не создавая новый список.

my_list = []
for num in range(1, 1001, 2):
    my_list.append(num ** 3)
# a
final_sum = 0
for num in my_list:
    check_sum = 0
    num_add = num
    while num_add > 0:
        check_num = num_add % 10
        num_add = num_add // 10
        check_sum += check_num

    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)

# b&c
final_sum = 0
for num in my_list:
    num += 17
    check_sum = 0
    num_add = num
    while num_add > 0:
        check_num = num_add % 10
        num_add = num_add // 10
        check_sum += check_num
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)