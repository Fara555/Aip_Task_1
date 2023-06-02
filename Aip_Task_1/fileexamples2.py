import os
#Вывести текущую рабочую директорию:
current_dir = os.getcwd()
print("Текущая рабочая директория:", current_dir)
#Создать новую директорию:
new_dir = "Новая_директория"
os.mkdir(new_dir)
print("Директория создана:", new_dir)
#Проверить существование файла или директории:
path = "путь_к_файлу_или_директории"
if os.path.exists(path):
    print("Файл или директория существует:", path)
else:
    print("Файл или директория не существует:", path)
#Получить список файлов и директорий в заданной директории:
directory = "путь_к_директории"
file_list = os.listdir(directory)
print("Список файлов и директорий:", file_list)
#Переименовать файл или директорию:
old_name = "старое_имя"
new_name = "новое_имя"
os.rename(old_name, new_name)
print("Файл или директория переименована:", old_name, "->", new_name)
#Удалить файл:
file_path = "путь_к_файлу"
os.remove(file_path)
print("Файл удален:", file_path)
#Удалить директорию:

directory = "путь_к_директории"
os.rmdir(directory)
print("Директория удалена:", directory)
#Получить информацию о файле:
file_path = "путь_к_файлу"
file_info = os.stat(file_path)
print("Информация о файле:", file_info)
#Изменить текущую рабочую директорию:
new_dir = "новая_директория"
os.chdir(new_dir)
print("Текущая рабочая директория изменена на:", new_dir)
#Получить имя файла из полного пути:
file_path = "полный_путь_к_файлу"
file_name = os.path.basename(file_path)
print("Имя файла из полного пути:", file_name)
#Получить расширение файла:
file_path = "полный_путь_к_файлу"
file_extension = os.path.splitext(file_path)[1]
print("Расширение файла:", file_extension)
#Проверить, является ли путь директорией:
path = "путь_к_файлу_или_директории"
if os.path.isdir(path):
    print("Путь является директорией:", path)
else:
    print("Путь не является директорией:", path)
#Проверить, является ли путь файлом:
path = "путь_к_файлу_или_директории"
if os.path.isfile(path):
    print("Путь является файлом:", path)
else:
    print("Путь не является файлом:", path)





