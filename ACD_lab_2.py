import numpy as np
import tkinter as tk
from tkinter import messagebox

# Генерація масиву
def generate_array():
    np.random.seed(0)  # Для відтворюваності результатів
    arr = np.random.randint(-10, 10, 15)

    # Гарантуємо наявність хоча б одного нуля та одиниці
    if 0 not in arr:
        arr[0] = 0
    if 1 not in arr:
        arr[1] = 1

    return arr

# Обчислення результатів
def calculate_results():
    arr = generate_array()

    max_abs_element = arr[0]  # Початкове значення для порівняння
    for num in arr:
        if abs(num) > abs(max_abs_element):
            max_abs_element = num
    # Знаходимо суму елементів між першим і другим додатними елементами
    positive_indices = [i for i, x in enumerate(arr) if x > 0]
    sum_between = sum(arr[positive_indices[0] + 1 : positive_indices[1]]) if len(positive_indices) > 1 else 0

    # Перетворюємо масив: нулі та одиниці переміщаємо в кінець
    transformed_arr = sorted(arr, key=lambda x: x in [0, 1])
    transformed_arr = [int(x) for x in transformed_arr]  # Перетворюємо на звичайні числа

    # Виводимо результати
    result_text = (
        f"Початковий масив: {arr}\n"
        f"Максимальний за модулем елемент: {max_abs_element}\n"
        f"Сума між першим і другим додатними елементами: {sum_between}\n"
        f"Перетворений масив: {transformed_arr}"
    )

    messagebox.showinfo("Результати", result_text)

    # Створення графічного інтерфейсу
root = tk.Tk()
root.title("Масив і обчислення")

# Кнопка для обчислення
button = tk.Button(root, text="Обчислити", command=calculate_results)
button.pack(pady=20)

# Запуск інтерфейсу
root.mainloop()
