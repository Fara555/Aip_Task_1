#Программа для замены слова или фразы в текстовом файле:
def replace_word(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        content = file.read()

    modified_content = content.replace(old_word, new_word)

    with open(file_path, 'w') as file:
        file.write(modified_content)

    print("Замена выполнена успешно.")


file_path = "путь_к_файлу"
old_word = input("Введите слово или фразу для замены: ")
new_word = input("Введите новое значение: ")

replace_word(file_path, old_word, new_word)

#Программа для подсчета количества строк в текстовом файле:
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_count = len(lines)

    print("Количество строк в файле:", line_count)


file_path = "путь_к_файлу"

count_lines(file_path)

#Программа для сортировки данных из одного файла и сохранения отсортированных значений в другом файле:
def sort_data(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()

    sorted_data = sorted(data)

    with open(output_file, 'w') as file:
        file.writelines(sorted_data)

    print("Сортировка выполнена успешно.")


input_file = "путь_к_входному_файлу"
output_file = "путь_к_выходному_файлу"

sort_data(input_file, output_file)

