# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


my_words = 0
my_lines = 0
with open(r".\5-2-in.txt", "r") as my_file:
    for line in my_file:
        my_lines += 1
        my_words += len(line.split())
print("Строк " + str(my_lines) + ", слов " + str(my_words))
