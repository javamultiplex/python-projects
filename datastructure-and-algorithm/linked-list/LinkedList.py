class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def to_list(self):
        node = self.head
        output = []
        while node:
            output.append(node.value)
            node = node.next
        return output

    def traverse(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(5)
    linked_list.traverse()

    print(linked_list.to_list())
