import timeit
import random
from tabulate import tabulate

def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sorted_data = sort_func(data[:])
    execution_time = timeit.default_timer() - start_time
    return sorted_data, execution_time


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:  
            lst[j + 1] = lst[j]  
            j -= 1
        lst[j + 1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2  
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]  
    return quick_sort(left) + middle + quick_sort(right)

# Генеруємо випадкові дані для тестування
data_smallest = [random.randint(0, 1_000) for _ in range(10)]
data_small = [random.randint(0, 1_000) for _ in range(100)]
data_big = [random.randint(0, 1_000) for _ in range(1_000)]
data_largest = [random.randint(0, 10_000) for _ in range(10_000)]

# Генерація частково відсортованих даних
data_almost_sorted = sorted(data_largest)
data_almost_sorted[int(len(data_almost_sorted) * 0.9):] = reversed(data_almost_sorted[int(len(data_almost_sorted) * 0.9):])

# Генерація реверсивно відсортованих даних
data_reversed = list(reversed(data_largest))

test_data = [
    ("Random Smallest", data_smallest),
    ("Random Small", data_small),
    ("Random Big", data_big),
    ("Random Largest", data_largest),
    ("Almost Sorted", data_almost_sorted),
    ("Reversed", data_reversed)
]

sorting_functions = [
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Timsort (built-in sorted)", sorted),
    ("Bubble Sort", bubble_sort),
    ("Shell Sort", shell_sort),
    ("Selection Sort", selection_sort)
]

# Проведення тестування та виведення результатів
table = []
headers = ["Sorting Algorithm"] + [name for name, _ in test_data]

for sort_name, sort_func in sorting_functions:
    row = [sort_name]
    for _, data in test_data:
        _, exec_time = measure_time(sort_func, data)
        row.append(f"{exec_time:.6f}")
    table.append(row)

print(tabulate(table, headers=headers, tablefmt="github"))







def linear_search(arr, target):
    return target in arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


A = [random.randint(0, 1_000) for _ in range(100)]
B = [random.randint(0, 1_000) for _ in range(100)]
A_sorted = insertion_sort(A[:])  # Копіюємо, щоб не змінювати оригінал
B_sorted = quick_sort(B[:])

while True:
    search_value = random.choice(A_sorted + B_sorted)
    linear_result_A = linear_search(A_sorted, search_value)
    binary_result_B = binary_search(B_sorted, search_value)
    
    if linear_result_A and binary_result_B:
        break

# Вивід результатів
print(f"Значення для пошуку: {search_value}")
print(f"Лінійний пошук у A: {'Знайдено' if linear_result_A else 'Не знайдено'}")
print(f"Бінарний пошук у B: {'Знайдено' if binary_result_B else 'Не знайдено'}")



D = [random.randint(0, 50) for _ in range(10)]
C = [random.randint(0, 50) for _ in range(10)]
D_sorted = insertion_sort(D[:])  # Копіюємо, щоб не змінювати оригінал
C_sorted = quick_sort(C[:])

while True:
    search_value = random.choice(D_sorted + C_sorted)
    linear_result_D = linear_search(D_sorted, search_value)
    binary_result_C = binary_search(C_sorted, search_value)
    
    if linear_result_D and binary_result_C:
        break

# Вивід результатів
print(f"Значення для пошуку: {search_value}")
print(f"Лінійний пошук у D: {'Знайдено' if linear_result_D else 'Не знайдено'}")
print(f"Бінарний пошук у C: {'Знайдено' if binary_result_C else 'Не знайдено'}")
print(D_sorted)
print(C_sorted)