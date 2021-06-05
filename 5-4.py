# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
my_file_in = open(r".\5-4-in.txt", "r", encoding='utf-8')
my_file_out = open(r".\5-4-out.txt", "w", encoding='utf-8')
content = my_file_in.readlines()
for line in content:
    my_buffer = line.split()
    my_buffer[0] = my_dict[my_buffer[0]]
    my_file_out.write(my_buffer[0] + " - " + my_buffer[2] + "\n")
