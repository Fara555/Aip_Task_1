import numpy as np

def count_elements_greater_than(array, threshold):
    count = np.sum(array > threshold)
    return count

# Пример использования
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
threshold_value = 5

result = count_elements_greater_than(my_array, threshold_value)
print("Количество элементов, больших", threshold_value, ":", result)
