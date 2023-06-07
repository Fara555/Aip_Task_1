#Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно. Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
def sum_range(start, end):
    if start > end:
        start, end = end, start  # Поменять значения местами, если start > end
    total = sum(range(start, end + 1))
    return total

# Пример использования функции
start = int(input("Введите начальное значение: "))
end = int(input("Введите конечное значение: "))

result = sum_range(start, end)
print("Сумма чисел от", start, "до", end, "включительно:", result)
#В данном примере функция sum_range() проверяет, если start больше end, меняет их местами. Затем она использует встроенную функцию sum() и функцию range() для суммирования всех целых чисел от start до end включительно. Результат выводится на экран с помощью функции print().


#Создайте пользовательскую функцию, принимающую произвольное количество аргументов и выводящую их затем на экран. Для вывода элементов полученного списка используйте цикл for. Вызовите функцию, передав ей в качестве значений целое число, вещественное число, строку и пустой список.
def print_arguments(*args):
    for arg in args:
        print(arg)

# Вызов функции с различными аргументами
print_arguments(10, 3.14, "Hello, World!", [])
#Функция print_arguments() определена с использованием *args, что позволяет ей принимать произвольное количество аргументов. Внутри функции мы просто проходимся по всем переданным аргументам с помощью цикла for и выводим их на экран с помощью функции print().

#Написать функцию для нахождение четных чисел массива
def find_even_numbers(arr):
    even_numbers = []
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
#Написать функцию для нахождение нечетных чисел массива
def find_odd_numbers(arr):
    odd_numbers = []
    for num in arr:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers
#Написать функцию для матрицы, элементы матрицы нужно ввести пользователь
def input_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input(f"Введите элемент [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)
    return matrix
#Напишите функцию, которая подсчитывает гласные и согласные в слове.
def count_vowels_consonants(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    consonants_count = 0

    for letter in word.lower():
        if letter in vowels:
            vowels_count += 1
        elif letter.isalpha():
            consonants_count += 1

    return vowels_count, consonants_count
#Пользователю будет предложено ввести слово. Затем функция count_vowels_consonants будет подсчитывать количество гласных и согласных букв в слове и возвращать их значения. Результаты будут выведены на экран.

#Напишите функцию для вывода степеней до введенного пользователя числа.
def print_powers(base, limit):
    power = 0
    result = 1

    while result <= limit:
        print(result)
        power += 1
        result = base ** power
#Пользователю будет предложено ввести число и верхнее ограничение. Затем функция print_powers будет выводить все степени числа, начиная с 1 и увеличивая показатель степени, пока результат не превысит заданное ограничение. Каждая степень будет выведена на экран.


#Напишите функцию, которая выводит сумму элементов
#Матрицы
def sum_matrix(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum
#Массив
def sum_array(array):
    total_sum = 0
    for element in array:
        total_sum += element
    return total_sum
#Количество слов в предложении
def count_words(sentence):
    words = sentence.split()
    return len(words)


