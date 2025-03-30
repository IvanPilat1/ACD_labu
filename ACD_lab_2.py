class DynamicArray:
    def __init__(self):
        self.data = []
    
    def display(self):
        print(self.data)
    
    def insert(self, index, value):
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            print("Індекс поза межами масиву")
    
    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
        else:
            print("Індекс поза межами масиву")
    
    def search_by_index(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            print("Індекс поза межами масиву")
            return None
    
    def search_by_value(self, value):
        indices = [i for i, x in enumerate(self.data) if x == value]
        return indices if indices else "Значення не знайдено"
    
    def max_abs_element(self):
        if not self.data:
            return None
        max_element = self.data[0]
        for num in self.data:
            if abs(num) > abs(max_element):
                max_element = num
        return max_element
    
    def sum_between_first_two_positives(self):
        pos_indices = [i for i, x in enumerate(self.data) if x > 0]
        if len(pos_indices) < 2:
            return 0
        return sum(self.data[pos_indices[0] + 1 : pos_indices[1]])
    
    def transform(self):
        others = [x for x in self.data if x not in (0, 1)]
        zeros_ones = [x for x in self.data if x in (0, 1)]
        self.data = others + zeros_ones

# Приклад використання
arr = DynamicArray()
arr.data = [3, 0, 1, -2, 5, 0, 7, 1, -3]
arr.display()
print("Максимальний за модулем елемент:", arr.max_abs_element())
print("Сума між першим і другим додатними елементами:", arr.sum_between_first_two_positives())
arr.transform()
arr.display()
