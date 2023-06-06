#1
def count_digits(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count

# Пример использования
my_string = "Hello123World456"
result = count_digits(my_string)
print("Количество цифр в строке:", result)

#2
def count_uppercase_letters(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

# Пример использования
my_string = "HelloWorld"
result = count_uppercase_letters(my_string)
print("Количество прописных букв в строке:", result)

#3
def count_lower_letters(string):
    count = 0
    for char in string:
        if char.islower() or char.isalpha() and char.isascii():
            count += 1
    return count

# Пример использования
my_string = "HelloПривет"
result = count_lower_letters(my_string)
print("Количество строчных букв в строке:", result)

#4
def convert_to_lowercase(string):
    return string.lower()

# Пример использования
my_string = "HelloWorld"
result = convert_to_lowercase(my_string)
print("Преобразованная строка:", result)


#5
def convert_to_uppercase(string):
    return string.upper()

# Пример использования
my_string = "ПриветWorld"
result = convert_to_uppercase(my_string)
print("Преобразованная строка:", result)


#6
def swap_case(string):
    return string.swapcase()

# Пример использования
my_string = "HelloПривет"
result = swap_case(my_string)
print("Преобразованная строка:", result)


#7
def print_digits(number):
    digits = str(number)
    for digit in reversed(digits):
        print(digit)

# Пример использования
my_number = 123456
print("Символы цифр числа:")
print_digits(my_number)


#8
def find_shortest_word(sentence):
    words = sentence.split()
    shortest_word = None
    for word in words:
        word = word.strip(",.!?")
        if not shortest_word or len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word

# Пример использования
my_sentence = "Это предложение с самым коротким словом"
result = find_shortest_word(my_sentence)
print("Самое короткое слово:", result)


#9
def count_punctuation_marks(sentence):
    punctuation_marks = ",.!?;:-"
    count = 0
    for char in sentence:
        if char in punctuation_marks:
            count += 1
    return count

# Пример использования
my_sentence = "Это предложение, содержащее знаки препинания!"
result = count_punctuation_marks(my_sentence)
print("Количество знаков препинания:", result)


#10
def remove_extra_spaces(sentence):
    return " ".join(sentence.split())

# Пример использования
my_sentence = "Это    предложение   с  избыточными   пробелами"
result = remove_extra_spaces(my_sentence)
print("Строка с одним пробелом между словами:", result)
