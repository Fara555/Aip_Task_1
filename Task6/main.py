import csv
#Чтение CSV файла и вывод его содержимого.

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
# Фильтрация данных в CSV файле на основе определенных условий.
def filter_csv_data(file_path, condition):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if condition(row):
                print(row)
# Сортировка данных в CSV файле по определенным столбцам.\
def sort_csv_data(file_path, sort_columns):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        sorted_rows = sorted(reader, key=lambda row: [row[col] for col in sort_columns])
        for row in sorted_rows:
            print(row)
# Группировка данных в CSV файле и выполнение агрегирующих операций (сумма, среднее значение, количество и т.д.).
from collections import defaultdict

def aggregate_csv_data(file_path, group_column, aggregate_column, aggregate_function):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        grouped_data = defaultdict(list)
        for row in reader:
            group_key = row[group_column]
            value = float(row[aggregate_column])  # Предполагается числовой столбец
            grouped_data[group_key].append(value)

        for group_key, values in grouped_data.items():
            result = aggregate_function(values)
            print(group_key, result)
# Добавление новых данных в существующий CSV файл.
def append_to_csv_file(file_path, data):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
#Удаление данных из CSV файла на основе заданных условий.
def delete_from_csv_file(file_path, condition):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if not condition(row)]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
# Создание нового CSV файла на основе выбранных столбцов из существующего файла.
def create_new_csv_file(file_path, selected_columns, new_file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        selected_rows = [[row[col] for col in selected_columns] for row in reader]

    with open(new_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(selected_rows)
