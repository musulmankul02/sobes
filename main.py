# 15)Подсчет количества слов в файле:
#    Создайте программу, которая подсчитывает количество слов в текстовом файле и выводит это число.
# 16)Запись в файл:   Попросите пользователя ввести некоторый текст и сохраните его в текстовом файле.
# 17)Копирование файла:
#    Напишите программу, которая копирует содержимое одного файла в другой файл.


############################################################
#16
# def i( nesw_file):
#     text = input('Введите текст: ')

#     with open(nesw_file, 'w') as neswfile:
#         neswfile.write(text)
# nesw_file = 'nesw.txt'

# i( nesw_file)


#################################################
# 17

# def copy_file(file_path, nesw_path):
#         with open(file_path, 'r') as source_file:
#             content = source_file.read()

#         with open(nesw_path, 'w') as destination_file:
#             destination_file.write(content)

#         print(f"Содержимое файла успешно скопировано из '{file_path}' в '{nesw_path}'.")

# file_path = 'text.txt'
# nesw_path = 'neswfile.txt'
# copy_file(file_path, nesw_path)