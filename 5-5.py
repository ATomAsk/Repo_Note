# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


import random

my_count = random.randint(5, 10)
is_first = True
my_sum = 0
with open(r".\5-5-out.txt", "w", encoding='utf-8') as my_file:
    while my_count > 0:
        if not is_first:
            my_file.write(" ")
        else:
            is_first = False
        my_number = random.randint(1, 10)
        my_sum += my_number
        my_file.write(str(my_number))
        my_count -= 1
print("Сумма = " + str(my_sum))
