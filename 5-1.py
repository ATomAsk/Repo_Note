# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

first_line = True
with open(r".\5-1-out.txt", "w") as my_file:
    while True:
        my_string = input("Введите строку (пустая строка - завершение): ")
        if my_string == "":
            break
        if not first_line:
            my_file.write("\n")
        else:
            first_line = False
        my_file.write(my_string)
