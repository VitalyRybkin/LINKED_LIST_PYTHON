class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        self.size += 1
        if self.head is None:
            self.head = self.Node(value)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value)
            prev = self.tail
            self.tail = self.tail.next
            self.tail.prev = prev

    def remove(self, value):
        if self.size == 0:
            self.head = self.tail = None
        else:
            find_node = self.head
            while find_node:
                if value == find_node.value:
                    print('Deleted -', find_node.value)
                    prev = find_node.prev
                    prev.next = find_node.next if find_node.next else None
                    self.size -= 1
                    break
                find_node = find_node.next
            else:
                print(f'{value} - not found')

    def print(self):
        print_node = self.head
        while print_node:
            print(print_node.value)
            print_node = print_node.next
        print(f'Size - {self.size}\n')

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.add('Coca-Cola')
    my_list.add('Sprite')
    my_list.add('Pepsi-Cola')
    my_list.print()
    my_list.remove('Pepsi-Cola')
    my_list.print()
    my_list.remove('Dr. Pepper')
    my_list.print()
