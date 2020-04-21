class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
        else:
            self.tail.next = DoubleNode(value)
            prev_node = self.tail
            self.tail = self.tail.next
            self.tail.previous = prev_node

    def traverse_forward(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def traverse_backward(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.previous


if __name__ == '__main__':
    double_linked_list = DoubleLinkedList()
    double_linked_list.append(1)
    double_linked_list.append(4)
    double_linked_list.append(9)
    print("***** Forward *****")
    double_linked_list.traverse_forward()
    print("***** Backward *****")
    double_linked_list.traverse_backward()
