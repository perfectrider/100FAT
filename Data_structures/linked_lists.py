
# 1. Single-linked list

class Node:
    def __init__(self, value=None):
        self.data_value = value
        self.next_value = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next_value = self.head_value
        self.head_value = new_node

    def push_end(self, new_data):
        new_node = Node(new_data)
        if self.head_value is None:
            self.head_value = new_node
            return
        last = self.head_value
        while last.next_value:
            last = last.next_value
        last.next_value = new_node

    def print_list(self):
        value_to_print = self.head_value
        while value_to_print is not None:
            print(value_to_print.data_value)
            value_to_print = value_to_print.next_value


class LLInterface:
    def __init__(self):
        self.linked_list = SingleLinkedList()

    def convert(self, iterable):
        self.linked_list.head_value = Node(iterable[0])
        nodes = [Node(value) for value in iterable]
        for index, node in enumerate(nodes):
            if index == 0:
                self.linked_list.head_value = node
            if index < len(nodes) - 1:
                node.next_value = nodes[index + 1]

    def print(self):
        self.linked_list.print_list()

    def push_left(self, value):
        self.linked_list.push_front(value)

    def push_right(self, value):
        self.linked_list.push_end(value)


ll_interface = LLInterface()
ll_interface.convert([1, 2, 3, 4, 5])
ll_interface.push_right(7)
ll_interface.push_left(3)
ll_interface.print()


# --------------------------------------------------------
# 2. Two-Linked List.

# class TLList:
#     class TLNode:
#         data_value = None
#         next_value = None
#         prev_value = None
#
#         def __init__(self, data_value, next_value=None, prev_value=None):
#             self.data_value = data_value
#             self.next_value = next_value
#             self.prev_value = prev_value
#
#     head = None
#     tail = None
#     length = 0
#
#     def add(self, data_value):
#         if not head:
#             self.head = TLList(data_value):
#             return data_value



