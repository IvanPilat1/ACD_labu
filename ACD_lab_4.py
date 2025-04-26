class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete_node(self, node):
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next

    def find_first_greater_than(self, value):
        curr = self.head
        while curr:
            if curr.data > value:
                return curr
            curr = curr.next
        return None

    def insert_before(self, node, data):
        if not node:
            return
        new_node = Node(data)
        new_node.next = node
        new_node.prev = node.prev
        if node.prev:
            node.prev.next = new_node
        else:
            self.head = new_node
        node.prev = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> " if curr.next else "\n")
            curr = curr.next




# завдання 1 
# Створення списку з цілих чисел
dll = DoublyLinkedList()
numbers = [1, 3, 5, 15, 2, 15, 7]
for num in numbers:
    dll.add_to_end(num)

print("Початковий список 1 :")
dll.print_list()

# Видалення першого елемента, більшого за 4
node_to_delete = dll.find_first_greater_than(4)
dll.delete_node(node_to_delete)

print("\nПісля видалення першого елемента > 4:")
dll.print_list()

# Вставити 10 перед кожним елементом рівним 15
curr = dll.head
while curr:
    if curr.data == 15:
        dll.insert_before(curr, 10)
        # пересуваємося через новий вставлений вузол
        curr = curr.next
    curr = curr.next

print("\nПісля вставки 10 перед кожним 15:")
dll.print_list()


# завдання 2
# Створення списку з дійсних чисел
dll2 = DoublyLinkedList()
numbers2 = [1.1, -2.0, 3.5, 4.4, -2.0, 5.5]
for num in numbers2:
    dll2.add_to_end(num)

print("\nПочатковий список 2:")
dll2.print_list()

# Видалення елемента перед кожним елементом із значенням -2
curr = dll2.head
while curr:
    if curr.data == -2.0 and curr.prev:
        dll2.delete_node(curr.prev)
    curr = curr.next

print("\nПісля видалення елемента перед -2:")
dll2.print_list()

# Вставка 33 в кінець списку
dll2.add_to_end(33.0)

print("\nПісля вставки 33 в кінець:")
dll2.print_list()
